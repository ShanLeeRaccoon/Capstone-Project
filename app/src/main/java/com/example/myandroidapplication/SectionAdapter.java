package com.example.myandroidapplication;

import android.bluetooth.BluetoothDevice;
import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.example.myandroidapplication.POJO.MyDistinctList;
import com.example.myandroidapplication.POJO.Section;

import java.util.List;

public class SectionAdapter extends RecyclerView.Adapter<SectionAdapter.SectionViewHolder> {
    public List<Section> sections;
    public Context context;

    public SectionAdapter (List<Section> sections, Context context) {
        this.sections = sections;
        this.context = context;
    }

    @NonNull
    @Override
    public SectionViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View section_view = LayoutInflater.from(parent.getContext()).inflate(R.layout.recycler_view_section, parent, false);
        return new SectionViewHolder(section_view);
    }

    @Override
    public void onBindViewHolder(@NonNull SectionViewHolder holder, int position) {
        Section section = sections.get(position);

        holder.header.setText(section.header);
        LinearLayoutManager layoutManager = new LinearLayoutManager(context);
        holder.recyclerView.setLayoutManager(layoutManager);
        holder.recyclerView.setAdapter(new ItemDeviceAdapter((MyDistinctList<BluetoothDevice>) section.devices, context, section.listener));
    }

    @Override
    public int getItemCount() {
        return this.sections.size();
    }

    public class SectionViewHolder extends RecyclerView.ViewHolder {
        private TextView header;
        private RecyclerView recyclerView;

        public SectionViewHolder(@NonNull View itemView) {
            super(itemView);
            this.header = itemView.findViewById(R.id.header);
            this.recyclerView = itemView.findViewById(R.id.recycler_view);
        }
    }
}
