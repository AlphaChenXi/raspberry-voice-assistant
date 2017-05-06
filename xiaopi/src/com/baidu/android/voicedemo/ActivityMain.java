package com.baidu.android.voicedemo;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceActivity;
import android.preference.PreferenceManager;
import com.baidu.speech.recognizerdemo.R;

/**
 * Created by weilikai01 on 2015/5/12.
 */
public class ActivityMain extends PreferenceActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        this.addPreferencesFromResource(R.xml.category);

        SharedPreferences sp = PreferenceManager.getDefaultSharedPreferences(this);
        sp.edit().remove(Constant.EXTRA_INFILE).commit(); // infile参数用于控制识别一个PCM音频流（或文件），每次进入程序都将该值清楚，以避免体验时没有使用录音的问题
    }
}
