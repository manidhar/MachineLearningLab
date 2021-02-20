package com.mani.ml.services;

import java.io.IOException;
import java.util.List;

import org.springframework.stereotype.Service;

import com.mani.ml.models.Car;

@Service
public class CarPricePredictorService {

	public String predictCarPrice(Car car) {
		ProcessBuilder processBuilder = new ProcessBuilder("python","hello.py");
	    processBuilder.redirectErrorStream(true);

	    Process process;
		try {
			process = processBuilder.start();
			System.out.println(process.getInputStream().toString());
			 List<String> results = readProcessOutput(process.getInputStream());

		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	    
		return "";
	}
}
