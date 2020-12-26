package com.example.myandroidapplication.POJO;

import android.bluetooth.BluetoothDevice;

import com.example.myandroidapplication.ItemDeviceAdapter;

import java.util.Set;

public class Section {
    public String header;
    public Set<BluetoothDevice> devices;
    public ItemDeviceAdapter.OnDeviceSelectClickListener listener;

    public Section(String header, Set<BluetoothDevice> devices, ItemDeviceAdapter.OnDeviceSelectClickListener listener) {
        this.header = header;
        this.devices = devices;
        this.listener = listener;
    }
}
