Please use your own certificate and keyfile instead of the examples included in this folder, and be sure to update the `logstash_ssl_*` variables in your playbook to use your files instead of these examples.

To generate a self-signed certificate/key pair, you can use use the command:

    $ sudo openssl req -x509 -batch -nodes -days 3650 -newkey rsa:2048 -keyout logstash-forwarder.key -out logstash-forwarder.crt
