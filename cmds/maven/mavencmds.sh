#!bin/bash

__maven_dependency_analyze(){
    mvn clean package -Dmaven.test.skip=true
}
register_command "dependency analyze" "__maven_dependency_analyze"

__maven_package(){
    mvn clean package -Dmaven.test.skip=true
}
register_command "package" "__maven_package"
register_command "code cp" "__maven_package"

__maven_compile(){
    mvn clean compile -Dmaven.test.skip=true
}
register_command "compile" "__maven_compile"
register_command "code cc" "__maven_compile"

__maven_clean(){
    mvn clean -Dmaven.test.skip=true
}
register_command "code c" "__maven_compile"
