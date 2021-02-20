package com.mani.ml.models;

import java.io.Serializable;

public class Car implements Serializable{
	
	private static final long serialVersionUID = -5553553344270974288L;
	private String year;
	private String shprice;
	private String kld;
	private String prevOwn;
	private String ftype;
	
	
	public String getYear() {
		return year;
	}
	public void setYear(String year) {
		this.year = year;
	}
	public String getShprice() {
		return shprice;
	}
	public void setShprice(String shprice) {
		this.shprice = shprice;
	}
	public String getKld() {
		return kld;
	}
	public void setKld(String kld) {
		this.kld = kld;
	}
	public String getPrevOwn() {
		return prevOwn;
	}
	public void setPrevOwn(String prevOwn) {
		this.prevOwn = prevOwn;
	}
	public String getFtype() {
		return ftype;
	}
	@Override
	public String toString() {
		return "Car [year=" + year + ", shprice=" + shprice + ", kld=" + kld + ", prevOwn=" + prevOwn + ", ftype="
				+ ftype + "]";
	}
	public void setFtype(String ftype) {
		this.ftype = ftype;
	}
	

}
