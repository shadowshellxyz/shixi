#!bin/bash

jarvis_maven_dependency_analyze(){
    mvn clean package -Dmaven.test.skip=true
}
register_command "dependency analyze" "jarvis_maven_dependency_analyze"

jarvis_maven_package(){
    mvn clean package -Dmaven.test.skip=true
}
register_command "package" "jarvis_maven_package"
register_command "code cp" "jarvis_maven_package"

jarvis_maven_compile(){
    mvn clean compile -Dmaven.test.skip=true
}
register_command "compile" "jarvis_maven_compile"
register_command "code cc" "jarvis_maven_compile"

jarvis_maven_clean(){
    mvn clean -Dmaven.test.skip=true
}
register_command "code c" "jarvis_maven_compile"
