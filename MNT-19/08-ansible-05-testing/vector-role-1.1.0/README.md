# Ansible-Vector role

Simple vector-server deploy and management role.

## Requirements

---

### Ansible

It was tested on the following versions:

* 2.12

### Operating systems

* Ubuntu 20.04
* Centos 8

## Role Variables

---

You can specify config Vector

```yaml
  vector_config:
    sources:
      our_log:
        type: file
        read_from: beginning
        ignore_older_secs: 600
        include:
          - /var/log/**/*.log
```

## Example Playbook

---

Just include this role in your list. For example:

```yaml
  - host: all
    roles:
      - vector
```

## License

---

MIT
