package com.stormadvance.kafka_producer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;


public class API 
{
	public static String getAPI()  throws IOException, ParseException 
	{
	    String data;
		
		URL urlForGetRequest = new URL("https://api.openweathermap.org/data/2.5/weather?id=2158177&units=metric&appid=ec22808df862ff0aa7e0601d85536ca4");
	    String readLine = null;
	    HttpURLConnection conection = (HttpURLConnection) urlForGetRequest.openConnection();
	    conection.setRequestMethod("GET");
	    int responseCode = conection.getResponseCode();

	    if (responseCode == HttpURLConnection.HTTP_OK) {
	        BufferedReader in = new BufferedReader(
	            new InputStreamReader(conection.getInputStream()));
	        StringBuffer response = new StringBuffer();
	        while ((readLine = in .readLine()) != null) {
	            response.append(readLine);
	        } in .close();
	        // print result
	        System.out.println("JSON String Result " + response.toString());
		    //Parse to JSON object to access nested data
	        JSONParser parser = new JSONParser();
	        //Get JSONobject from response
		    JSONObject JSON = (JSONObject) parser.parse(response.toString());
		    //Access 'main' data
		    JSONObject main = (JSONObject) JSON.get("main");
		    //Access wind data 
		    JSONObject wind = (JSONObject) JSON.get("wind");
		    data = main.get("temp").toString();
		    data += ", " + main.get("pressure").toString();
		    data += ", " + main.get("humidity").toString();
		    data += ", " + wind.get("speed").toString();
		    data += ", " + wind.get("deg").toString();
		    return data;

	    } else {
	        return "API failed";
	    }
	}
}

