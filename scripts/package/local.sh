#!/usr/bin/env bash

cd ../..
mvn clean package install -Dmaven.test.skip=true