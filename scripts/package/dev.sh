#!/usr/bin/env bash
mvn clean -U -Pdev package -Dmaven.test.skip=false

mvn clean compile -U Dmaven.test.skip=true