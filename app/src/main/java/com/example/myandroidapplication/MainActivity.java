package com.example.myandroidapplication;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.Manifest;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothSocket;
import android.companion.CompanionDeviceManager;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.pm.PackageManager;
import android.location.LocationManager;
import android.os.Bundle;
import android.provider.Settings;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import com.example.myandroidapplication.POJO.MyDistinctList;
import com.example.myandroidapplication.POJO.Section;

import java.io.IOException;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Set;
import java.util.UUID;

public class MainActivity extends AppCompatActivity implements ItemDeviceAdapter.OnDeviceSelectClickListener {
//    private BluetoothHeadset bluetoothHeadset;
//    private BluetoothProfile.ServiceListener profileListener = new BluetoothProfile.ServiceListener() {
//        @Override
//        public void onServiceConnected(int profile, BluetoothProfile proxy) {
//            if (profile == BluetoothProfile.HEADSET) {
//                bluetoothHeadset = (BluetoothHeadset) proxy;
//            }
//        }
//
//        @Override
//        public void onServiceDisconnected(int profile) {
//            if (profile == BluetoothProfile.HEADSET) {
//                bluetoothHeadset = null;
//            }
//        }
//    };

    private final int BLUETOOTH_REQUEST_CODE = 1;
    private final int SELECT_DEVICE_REQUEST_CODE = 42;
    private final int PERMISSIONS_REQUEST_ACCESS_FINE_LOCATION = 2;
    private final int TURN_ON_LOCATION_SERVICE = 3;

    private BluetoothAdapter bluetoothAdapter;
    private BroadcastReceiver bluetoothReceiver = new BroadcastReceiver() {
        @Override
        public void onReceive(Context context, Intent intent) {
            String action = intent.getAction();
            if (BluetoothAdapter.ACTION_DISCOVERY_STARTED.equals(action)) {
                Toast.makeText(context, "Discovery started", Toast.LENGTH_LONG).show();
            } else if (BluetoothAdapter.ACTION_DISCOVERY_FINISHED.equals(action)) {
                Toast.makeText(context, "Discovery finished", Toast.LENGTH_LONG).show();
            } else if (BluetoothDevice.ACTION_FOUND.equals(action)) {
                BluetoothDevice device = intent.getParcelableExtra(BluetoothDevice.EXTRA_DEVICE);
                foundDevices.add(device);
                sectionAdapter.notifyItemChanged(1);
            } else {
                Toast.makeText(context, "No Bluetooth Devices detected.", Toast.LENGTH_LONG).show();
            }
        }
    };

    private Set<BluetoothDevice> foundDevices = new MyDistinctList<>();
    private Set<BluetoothDevice> pairedDevices = new MyDistinctList<>();
    private Section foundSection, pairedSection;

    public static UUID uuid_in_bluedot = UUID.fromString("00001101-0000-1000-8000-00805f9b34fb");

    SectionAdapter sectionAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        bluetoothAdapter = BluetoothAdapter.getDefaultAdapter();

        //Register a Bluetooth Receiver
        IntentFilter filter = new IntentFilter();
        filter.addAction(BluetoothDevice.ACTION_FOUND);
        filter.addAction(BluetoothAdapter.ACTION_DISCOVERY_STARTED);
        filter.addAction(BluetoothAdapter.ACTION_DISCOVERY_FINISHED);
        registerReceiver(bluetoothReceiver, filter);

        // Turn on Bluetooth button
        Button btTurnOnBluetooth = findViewById(R.id.button);
        btTurnOnBluetooth.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (!bluetoothAdapter.isEnabled()){
                    Intent enableBtIntent = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
                    startActivityForResult(enableBtIntent, BLUETOOTH_REQUEST_CODE);
                }
                else {
                    Toast.makeText(getApplicationContext(), "Bluetooth is already turned on", Toast.LENGTH_LONG).show();
                }
            }
        });

        // Turn on ScanNearby button
        Button btScanNearbyDevices = findViewById(R.id.button2);
        btScanNearbyDevices.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                foundDevices.clear();
                pairedDevices.addAll(bluetoothAdapter.getBondedDevices());
                sectionAdapter.notifyDataSetChanged();

                Toast.makeText(MainActivity.this, "Scanning: " + bluetoothAdapter.startDiscovery(), Toast.LENGTH_SHORT).show();
            }
        });

        // Turn on Location button
        Button btTurnOnLocation = findViewById(R.id.button3);
        btTurnOnLocation.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (!(ContextCompat.checkSelfPermission(getApplicationContext(), android.Manifest.permission.ACCESS_FINE_LOCATION) == PackageManager.PERMISSION_GRANTED)) {
                    // This code will pop up and ask for location request
                    ActivityCompat.requestPermissions(MainActivity.this, new String[]{Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_COARSE_LOCATION}, TURN_ON_LOCATION_SERVICE);
                } else {
                    turnOnBluetoothService();
                    Toast.makeText(MainActivity.this, "Location service is permitted", Toast.LENGTH_SHORT).show();
                }
            }
        });

        // RecyclerView
        foundSection = new Section("Available Devices", foundDevices, this);
        pairedSection = new Section("Paired Devices", pairedDevices, this);
        List<Section> sections = Arrays.asList(pairedSection, foundSection);

        //Set basic Adapter and Layout Manager
        LinearLayoutManager layoutManager = new LinearLayoutManager(this);
        RecyclerView recyclerView = findViewById(R.id.main_recycler);
        sectionAdapter = new SectionAdapter(sections, getBaseContext());
        recyclerView.setAdapter(sectionAdapter);
        recyclerView.setLayoutManager(layoutManager);
//        // Set Divider Item Decoration
//        DividerItemDecoration divider = new DividerItemDecoration(recyclerView.getContext(), DividerItemDecoration.VERTICAL);
//        Drawable drawable = getApplicationContext().getDrawable(R.drawable.row_divider);
//        divider.setDrawable(drawable);
//        recyclerView.addItemDecoration(divider);
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        switch (requestCode){
            case TURN_ON_LOCATION_SERVICE:
                boolean permitted = true;
                for(int i: grantResults){
                    permitted &= (i == PackageManager.PERMISSION_GRANTED);
                }

                if (permitted){
                    Toast.makeText(this, "Location permissions granted", Toast.LENGTH_SHORT).show();
                    turnOnBluetoothService();
                } else {
                    if (ActivityCompat.shouldShowRequestPermissionRationale(MainActivity.this, Manifest.permission.ACCESS_FINE_LOCATION)){
                        Toast.makeText(MainActivity.this, "Please allow us to turn on! Or it won't work!", Toast.LENGTH_LONG).show();
                    } else {
                        Toast.makeText(this, "Location permissions not granted", Toast.LENGTH_SHORT).show();
                    }
                }
                break;
            default:
                break;
        }
    }

    private void turnOnBluetoothService(){
        if (!(((LocationManager) getSystemService(Context.LOCATION_SERVICE)).isProviderEnabled(LocationManager.GPS_PROVIDER))) {
            // This code moves the user to Settings of the App in Android
            Intent enableLocationIntent = new Intent(Settings.ACTION_LOCATION_SOURCE_SETTINGS);
            startActivityForResult(enableLocationIntent, TURN_ON_LOCATION_SERVICE);
        }
    }

    @Override
    protected void onDestroy() {
        unregisterReceiver(bluetoothReceiver);
        super.onDestroy();
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        switch (requestCode){
            case BLUETOOTH_REQUEST_CODE:
                if (resultCode == RESULT_OK) {
                    Toast.makeText(this, "User accepts to turn Bluetooth on", Toast.LENGTH_LONG).show();
                }
                else {
                    Toast.makeText(this, "User doesn't allow to turn Bluetooth on", Toast.LENGTH_LONG).show();
                }
                break;

            case SELECT_DEVICE_REQUEST_CODE:
                if (resultCode == RESULT_OK) {
                    BluetoothDevice deviceToPair = data.getParcelableExtra(CompanionDeviceManager.EXTRA_DEVICE);
                    deviceToPair.createBond();
                    Toast.makeText(this, "Create bond with devices", Toast.LENGTH_LONG).show();
                }
                else {
                    Toast.makeText(this, "User doesn't allow to turn Bluetooth on", Toast.LENGTH_LONG).show();
                }
                break;

            case TURN_ON_LOCATION_SERVICE:
                break;

            default:
                Toast.makeText(this, "Result from somewhere I don't know: " + requestCode, Toast.LENGTH_SHORT).show();
        }
        super.onActivityResult(requestCode, resultCode, data);
    }

    @Override
    public void onDeviceClick(int position) {
//        Toast.makeText(this, String.valueOf(position), Toast.LENGTH_SHORT).show();
//            if (bluetoothAdapter.isDiscovering()) bluetoothAdapter.cancelDiscovery();
//
//            BluetoothDevice pi = bluetoothAdapter.getRemoteDevice("DC:A6:32:0A:66:80"), device = foundDevices.get(position);
//            try (BluetoothSocket socket = pi.createRfcommSocketToServiceRecord(uuid_in_bluedot)){
//                socket.connect();
//                OutputStream stream = socket.getOutputStream();
//                stream.write(device.getAddress().getBytes());
//            } catch (IOException e) {
//                e.printStackTrace();
//            } finally {
//
//            }
    }

    @Override
    public void onDeviceClick(BluetoothDevice device) {
        Toast.makeText(this, device.getAddress(), Toast.LENGTH_SHORT).show();

        if (bluetoothAdapter.isDiscovering()) bluetoothAdapter.cancelDiscovery();

        BluetoothDevice pi = bluetoothAdapter.getRemoteDevice("DC:A6:32:0A:66:80");
        try (BluetoothSocket socket = pi.createRfcommSocketToServiceRecord(uuid_in_bluedot)){
            socket.connect();
            OutputStream stream = socket.getOutputStream();
            stream.write(device.getAddress().getBytes());
        } catch (IOException e) {
            e.printStackTrace();
        } finally {

        }
    }
}