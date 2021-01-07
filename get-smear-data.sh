#!/bin/bash

urlbase="https://avaa.tdata.fi/smear-services/smeardata.jsp?table=KUM_META&variables="

variables="NO_x,NO,O_3,SO_2,CO,p,rh,t,PM10_TEOM,PM25_TEOM,ws,wdir,rmm"

from="2018-03-01"
to="2020-12-31"
suffix="&quality=Any&averaging=NONE&type=NONE&format=csv"

request="${urlbase}${variables}&from=${from}%2000:00:00&to=${to}%2000:00:00${suffix}"

wget -O "smeardata-$from-to-$to.csv" "${request}"
