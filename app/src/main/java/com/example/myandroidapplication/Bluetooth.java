//package com.example.myandroidapplication;
//
//import android.bluetooth.BluetoothDevice;
//import android.bluetooth.BluetoothSocket;
//import android.os.Bundle;
//import android.os.Handler;
//import android.os.Message;
//import android.util.Log;
//
//import java.io.IOException;
//import java.io.InputStream;
//import java.io.OutputStream;
//import java.util.Optional;
//import java.util.UUID;
//
//public class Bluetooth {
//    /**
//     * This class helps create bonds between sockets
//     */
//    public static class ClientConnection extends Thread {
//        private String TAG = "BLUETOOTH CLIENT";
//        public BluetoothSocket socket;
//        public BluetoothDevice device;
//
//        public ClientConnection(BluetoothDevice device, UUID uuid) {
//            this.device = device;
//            this.socket = null;
//
//            try {
//                this.socket = device.createRfcommSocketToServiceRecord(uuid);
//            } catch (IOException e) {
//                e.printStackTrace();
//            }
//        }
//
//        @Override
//        public void run() {
//            try {
//                this.socket.connect();
//            } catch (IOException | NullPointerException e) {
//                e.printStackTrace();
//
//                try {
//                    this.socket.close();
//                } catch (IOException exception) {
//                    Log.e(TAG, "Could not even close client socket");
//                    exception.printStackTrace();
//                }
//            }
//        }
//
//        public void cancel() {
//            try {
//                this.socket.close();
//            } catch (IOException e) {
//                Log.e(TAG, "Could not close the client socket", e);
//            }
//        }
//    }
//
//    public static class TransferData {
//        private String TAG = "TRANSFER_DATA";
//        private Handler handler;
//
//        private interface MessageConstants {
//            public static final int MESSAGE_READ = 0;
//            public static final int MESSAGE_WRITE = 1;
//            public static final int MESSAGE_TOAST = 2;
//
//            // ... (Add other message types here as needed.)
//        }
//
//        public BluetoothSocket socket;
//        public InputStream inputStream;
//        public OutputStream outputStream;
//        private byte[] mmBuffer;
//
//        public TransferData (BluetoothSocket socket) {
//            this.socket = socket;
//
//            try {
//                inputStream = socket.getInputStream();
//            } catch (IOException e) {
//                e.printStackTrace();
//            }
//
//            try {
//                outputStream = socket.getOutputStream();
//            } catch (IOException e) {
//                e.printStackTrace();
//            }
//        }
//
//        public void run() {
//            mmBuffer = new byte[1024];
//            int numBytes; // bytes returned from read()
//
//            // Keep listening to the InputStream until an exception occurs.
//            while (true) {
//                try {
//                    // Read from the InputStream.
//                    numBytes = inputStream.read(mmBuffer);
//                    // Send the obtained bytes to the UI activity.
//                    Message readMsg = handler.obtainMessage(
//                            MessageConstants.MESSAGE_READ, numBytes, -1,
//                            mmBuffer);
//                    readMsg.sendToTarget();
//                } catch (IOException e) {
//                    Log.d(TAG, "Input stream was disconnected", e);
//                    break;
//                }
//            }
//        }
//
//        // Call this from the main activity to send data to the remote device.
//        public void write(byte[] bytes) {
//            try {
//                outputStream.write(bytes);
//
//                // Share the sent message with the UI activity.
//                Message writtenMsg = handler.obtainMessage(
//                        MessageConstants.MESSAGE_WRITE, -1, -1, bytes);
//                writtenMsg.sendToTarget();
//            } catch (IOException e) {
//                Log.e(TAG, "Error occurred when sending data", e);
//
//                // Send a failure message back to the activity.
//                Message writeErrorMsg =
//                        handler.obtainMessage(MessageConstants.MESSAGE_TOAST);
//                Bundle bundle = new Bundle();
//                bundle.putString("toast",
//                        "Couldn't send data to the other device");
//                writeErrorMsg.setData(bundle);
//                handler.sendMessage(writeErrorMsg);
//            }
//        }
//
//        // Call this method from the main activity to shut down the connection.
//        public void cancel() {
//            try {
//                this.socket.close();
//            } catch (IOException e) {
//                Log.e(TAG, "Could not close the connect socket", e);
//            }
//        }
//    }
//}
