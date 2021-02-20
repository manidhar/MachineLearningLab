package com.mani.ml.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import com.mani.ml.models.Car;
import com.mani.ml.services.CarPricePredictorService;


@RestController
@RequestMapping("/ml-service")
@CrossOrigin(origins = "*", allowedHeaders = "*")
public class CarPriceController {
	
	@Autowired
	private CarPricePredictorService cps;
	
	@RequestMapping(method=RequestMethod.POST,value="/carprice")
	public String predictCarPrice(@RequestBody Car car){
		try {
			
			return cps.predictCarPrice(car);
			
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
	}

}
