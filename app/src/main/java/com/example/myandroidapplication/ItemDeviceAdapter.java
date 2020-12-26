package com.example.myandroidapplication;

import android.bluetooth.BluetoothClass;
import android.bluetooth.BluetoothDevice;
import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.example.myandroidapplication.POJO.MyDistinctList;

import java.util.List;
import java.util.Set;

//Tutorial from Google
//https://developer.android.com/guide/topics/ui/layout/recyclerview
public class ItemDeviceAdapter extends RecyclerView.Adapter<ItemDeviceAdapter.ItemDeviceViewHolder> {
    MyDistinctList<BluetoothDevice> devices;
    OnDeviceSelectClickListener listener;
    Context context;

    public ItemDeviceAdapter(MyDistinctList<BluetoothDevice> devices, Context context, OnDeviceSelectClickListener listener) {
        this.context = context;
        this.devices = devices;
        this.listener = listener;
    }

    @NonNull
    @Override
    public ItemDeviceViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View deviceView = LayoutInflater.from(parent.getContext()).inflate(R.layout.row, parent, false);
        return new ItemDeviceViewHolder(deviceView);
    }

    @Override
    public void onBindViewHolder(@NonNull ItemDeviceViewHolder holder, int position) {
        BluetoothDevice device = devices.get(position);

        holder.address.setText(device.getAddress());
        holder.name.setText(device.getName());

        int deviceClass =  device.getBluetoothClass().getMajorDeviceClass();
        holder.type.setText(String.valueOf(deviceClass));
        holder.imageView.setImageDrawable(context.getDrawable(getCorrectDrawable(deviceClass)));


        holder.itemView.setOnClickListener(v -> {
            listener.onDeviceClick(device);

//            BluetoothDevice device1 = (BluetoothDevice) holder.itemView.getTag();
//            Toast.makeText(v.getContext(), "Click on Device Name: " + device1.getName(), Toast.LENGTH_SHORT).show();
        });
    }

    public int getCorrectDrawable(int deviceClass) {
        switch (deviceClass) {
            case BluetoothClass.Device.Major.COMPUTER:
                return R.drawable.ic_baseline_computer_24;

            case BluetoothClass.Device.Major.AUDIO_VIDEO:
                return R.drawable.ic_baseline_hearing_24;

            case BluetoothClass.Device.Major.PHONE:
                return R.drawable.ic_baseline_smartphone_24;

            case BluetoothClass.Device.Major.WEARABLE:
                return R.drawable.ic_baseline_wearable_24;

            default:
                return R.drawable.ic_baseline_other_devices_24;
        }
    }

    @Override
    public int getItemCount() {
        return devices.size();
    }

    static class ItemDeviceViewHolder extends RecyclerView.ViewHolder {
        public TextView name, address, type;
        public ImageView imageView;

        public ItemDeviceViewHolder(@NonNull View itemView) {
            super(itemView);

            name = itemView.findViewById(R.id.name);
            address = itemView.findViewById(R.id.address);
            type = itemView.findViewById(R.id.type);
            imageView = itemView.findViewById(R.id.imageView);
        }


    }

    public interface OnDeviceSelectClickListener {
        /**
         * Apply dependency injection for ClickListener of Adapter
         * @param position current index of item in the list, not the x, y position, so don't worry
         */
        void onDeviceClick(int position);
        void onDeviceClick(BluetoothDevice device);
    }
}

