package com.example.myandroidapplication.POJO;

import java.util.Iterator;
import java.util.LinkedHashSet;
import java.util.List;

public class MyDistinctList<E> extends LinkedHashSet<E> {
    public E get(int index) {
        Iterator<E> iter = super.iterator();
        for (int i = 0; i < index; i++) {
            if (iter.hasNext()) {
                iter.next();
            }
        }

        return iter.next();
    }
}
