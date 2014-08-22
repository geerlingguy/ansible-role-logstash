# Ansible Role: Logstash

[![Build Status](https://travis-ci.org/geerlingguy/ansible-role-logstash.svg?branch=master)](https://travis-ci.org/geerlingguy/ansible-role-logstash)

An Ansible Role that installs Logstash on Debian/Ubuntu.

**Note**: This role is under active development and is not considered stable quite yet. I am working on making sure it runs across a wider variety of platforms, and also will work with different kinds of workflows you may have. Please file issues on GitHub if you find a problem!

**Security Note**: Until this role reaches a stable release, please consider it insecure, and do not use it on any production systems. Things like SSL and certificates are not being used for message authentication at this time!

## Requirements

Though other methods are possible, this role is made to work with Elasticsearch as a backend for storing log messages.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    logstash_listen_port_tcp: 5000
    logstash_listen_port_udp: 5000

The TCP and UDP ports over which logstash will listen for syslog messages.

    logstash_elasticsearch_host: localhost

The host on which Elasticsearch resides.

## Dependencies

  - geerlingguy.elasticsearch

## Example Playbook

    - hosts: search
      roles:
        - { role: geerlingguy.elasticsearch }
        - { role: geerlingguy.logstash }

## License

MIT / BSD

## Author Information

This role was created in 2014 by [Jeff Geerling](http://jeffgeerling.com/), author of [Ansible for DevOps](http://ansiblefordevops.com/).
