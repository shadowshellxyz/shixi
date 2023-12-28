#!bin/bash
# author:shadow walker

NGINX_HOME=/usr/local/nginx
NGINX_CONF_HOME=$NGINX_HOME/conf/nginx.conf

nginx_start(){

    $NGINX_HOME/sbin/nginx -c $NGINX_CONF_HOME
}

nginx_stop(){

    $NGINX_HOME/sbin/nginx -s stop
}

nginx_reload(){

    nginx_cfg_refresh
    
    $NGINX_HOME/sbin/nginx -s reload -c $NGINX_CONF_HOME
}

nginx_cfg(){

    $NGINX_HOME/sbin/nginx -tc $NGINX_CONF_HOME
}

nginx_cfg_refresh(){

    alias cp='cp'
    cp -f $SHIXI_HOME/shixi/.shixi/cmd/nginx/nginx.conf $NGINX_HOME/conf/
    alias cp='cp -i'
}

nginx_healthy(){

    ps -aux | grep nginx

}


