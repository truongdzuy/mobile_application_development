package com.example.truongdangduy.androidtraining;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {
    Button button;
    Spinner spinner;
    EditText inputNum;
    TextView outputNum;
    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        button = (Button)findViewById(R.id.button);
        spinner = (Spinner)findViewById(R.id.spinner);
        inputNum = (EditText)findViewById(R.id.inputText);
        outputNum = (TextView)findViewById(R.id.outputText);
        final float ratio[] = new float[4];
        ratio[0]=(float)(1 / 22727.2727);
        ratio[1]=(22727.2727f);
        ratio[2]=(float)(1/211.863636);
        ratio[3]=(211.863636f);
        button.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v) {
                int i=0;
                switch (spinner.getSelectedItem().toString())
                {
                    case "VND->USD":
                        i=0;
                        break;
                    case "USD->VND":
                        i=1;
                        break;
                    case "VND->JPY":
                        i=2;
                        break;
                    case "JPY->VND":
                        i=3;
                        break;
                }
                Log.d("message",inputNum.getText().toString());
                Float exchangeNum = Float.valueOf(inputNum.getText().toString())*ratio[i];
                outputNum.setText(exchangeNum.toString());
            }
        });
    }
}
