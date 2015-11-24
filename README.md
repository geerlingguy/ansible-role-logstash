# Ansible Role: Logstash

[![Build Status](https://travis-ci.org/geerlingguy/ansible-role-logstash.svg?branch=master)](https://travis-ci.org/geerlingguy/ansible-role-logstash)

An Ansible Role that installs Logstash on RedHat/CentOS Debian/Ubuntu.

Note that this role installs a syslog grok pattern by default; if you want to add more filters, please add them inside the `/etc/logstash/conf.d/` directory. As an example, you could create a file named `13-myapp.conf` with the appropriate grok filter and restart logstash to start using it. Test your grok regex using the [Grok Debugger](http://grokdebug.herokuapp.com/).

## Requirements

Though other methods are possible, this role is made to work with Elasticsearch as a backend for storing log messages.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    logstash_listen_port_tcp: 5000
    logstash_listen_port_udp: 5000

The TCP and UDP ports over which logstash will listen for syslog messages.

    logstash_elasticsearch_host: localhost

The host on which Elasticsearch resides.

    logstash_ssl_dir: /etc/pki/logstash
    logstash_ssl_certificate_file: logstash-forwarder-example.crt
    logstash_ssl_key_file: logstash-forwarder-example.key

SSL configuration for Logstash to accept requests from logstash-forwarder running on remote hosts. **Security note**: On production or public-facing (e.g. any non-test) servers, you should create your own key/certificate pair and use that instead of the included default! You can use OpenSSL to create the key and certificate files, with a command like the following: `openssl req -x509  -batch -nodes -newkey rsa:2048 -keyout lumberjack.key -out lumberjack.crt -subj /CN=logstash.example.com`.

For the `logstash_ssl_certificate_file` and `logstash_ssl_key_file`, you can provide a path relative to the role directory, or an absolute path to the file.

    logstash_local_syslog_path: /var/log/syslog
    logstash_monitor_local_syslog: true

Whether configuration for local syslog file (defined as `logstash_local_syslog_path`) should be added to logstash. Set this to `false` if you are monitoring the local syslog differently, or if you don't care about the local syslog file. Other local logs can be added by your own configuration files placed inside `/etc/logstash/conf.d`.

    logstash_enabled_on_boot: yes

Set this to `no` if you don't want logstash to run on system startup.

## Other Notes

If you are seeing high CPU usage from one of the `logstash` processes, and you're using Logstash along with another application running on port 80 on a platform like Ubuntu with upstart, the `logstash-web` process may be stuck in a loop trying to start on port 80, failing, and trying to start again, due to the `restart` flag being present in `/etc/init/logstash-web.conf`. To avoid this problem, either change that line to add a `limit` to the respawn statement, or set the `logstash-web` service to `enabled=no` in your playbook, e.g.:

    - name: Ensure logstash-web process is stopped and disabled.
      service: name=logstash-web state=stopped enabled=no


## Example Playbook

    - hosts: search
      roles:
        - { role: geerlingguy.elasticsearch }
        - { role: geerlingguy.logstash }

## License

MIT / BSD

## Author Information

This role was created in 2014 by [Jeff Geerling](http://jeffgeerling.com/), author of [Ansible for DevOps](http://ansiblefordevops.com/).
