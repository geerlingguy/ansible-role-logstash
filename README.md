# Ansible Role: Logstash

[![Build Status](https://travis-ci.org/geerlingguy/ansible-role-logstash.svg?branch=master)](https://travis-ci.org/geerlingguy/ansible-role-logstash)

An Ansible Role that installs Logstash on RedHat/CentOS Debian/Ubuntu.

Note that this role installs a syslog grok pattern by default; if you want to add more filters, please add them inside the `/etc/logstash/conf.d/` directory. As an example, you could create a file named `13-myapp.conf` with the appropriate grok filter and restart logstash to start using it. Test your grok regex using the [Grok Debugger](http://grokdebug.herokuapp.com/).

## Requirements

Though other methods are possible, this role is made to work with Elasticsearch as a backend for storing log messages.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    logstash_listen_port_beats: 5044

The port over which Logstash will listen for beats.

    logstash_elasticsearch_hosts:
      - http://localhost:9200

The hosts where Logstash should ship logs to Elasticsearch.

    logstash_dir: /usr/share/logstash

The directory inside which Logstash is installed.

    logstash_ssl_dir: /etc/pki/logstash
    logstash_ssl_certificate_file: logstash-forwarder-example.crt
    logstash_ssl_key_file: logstash-forwarder-example.key

Local paths to the SSL certificate and key files, which will be copied into the `logstash_ssl_dir`.

For utmost security, you should use your own valid certificate and keyfile, and update the `logstash_ssl_*` variables in your playbook to use your certificate.

To generate a self-signed certificate/key pair, you can use use the command:

    $ sudo openssl req -x509 -batch -nodes -days 3650 -newkey rsa:2048 -keyout logstash.key -out logstash.crt

Note that filebeat and logstash may not work correctly with self-signed certificates unless you also have the full chain of trust (including the Certificate Authority for your self-signed cert) added on your server. See: https://github.com/elastic/logstash/issues/4926#issuecomment-203936891

    logstash_local_syslog_path: /var/log/syslog
    logstash_monitor_local_syslog: true

Whether configuration for local syslog file (defined as `logstash_local_syslog_path`) should be added to logstash. Set this to `false` if you are monitoring the local syslog differently, or if you don't care about the local syslog file. Other local logs can be added by your own configuration files placed inside `/etc/logstash/conf.d`.

    logstash_enabled_on_boot: true

Set this to `false` if you don't want logstash to run on system startup.

    logstash_install_plugins:
      - logstash-input-beats

A list of Logstash plugins that should be installed.

## Other Notes

If you are seeing high CPU usage from one of the `logstash` processes, and you're using Logstash along with another application running on port 80 on a platform like Ubuntu with upstart, the `logstash-web` process may be stuck in a loop trying to start on port 80, failing, and trying to start again, due to the `restart` flag being present in `/etc/init/logstash-web.conf`. To avoid this problem, either change that line to add a `limit` to the respawn statement, or set the `logstash-web` service to `enabled=no` in your playbook, e.g.:

    - name: Ensure logstash-web process is stopped and disabled.
      service: name=logstash-web state=stopped enabled=no

## Example Playbook

    - hosts: search
      roles:
        - geerlingguy.elasticsearch
        - geerlingguy.logstash

## License

MIT / BSD

## Author Information

This role was created in 2014 by [Jeff Geerling](https://www.jeffgeerling.com/), author of [Ansible for DevOps](https://www.ansiblefordevops.com/).
