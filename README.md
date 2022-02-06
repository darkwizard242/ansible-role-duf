[![build-test](https://github.com/darkwizard242/ansible-role-duf/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-duf/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-duf/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-duf/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/56561?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/56561?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/56561?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-duf&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-duf) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-duf&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-duf) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-duf&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-duf) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-duf&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-duf) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-duf?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-duf?color=orange&style=flat-square)

# Ansible Role: duf

Role to install (_by default_) [duf](https://github.com/muesli/duf) on **Debian/Ubuntu** and **EL** systems. A better alternative to 'df'.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
duf_app: duf
duf_desired_state: present
duf_version: 0.8.0
duf_os: "linux"
duf_arch: "amd64"

# For Debian/Ubuntu Family
duf_debian_url: "https://github.com/muesli/{{ duf_app }}/releases/download/v{{ duf_version }}/{{ duf_app }}_{{ duf_version }}_{{ duf_os }}_{{ duf_arch }}.deb"

# For EL Family
duf_el_url: "https://github.com/muesli/{{ duf_app }}/releases/download/v{{ duf_version }}/{{ duf_app }}_{{ duf_version }}_{{ duf_os }}_{{ duf_arch }}.rpm"
```

### Variables table:

Variable          | Description
----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------
duf_app           | Defines the app to install i.e. **duf**
duf_desired_state | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Defaults to `present`.
duf_version       | Defined to dynamically fetch the desired version to install. Defaults to: **0.8.0**
duf_os            | Defines OS type. Used for obtaining the correct type of binaries based on OS. Defaults to: **linux**
duf_arch          | Defines Architecture type. Used for obtaining the correct type of binaries based on Architecture. Defaults to: **amd64**
duf_debian_url    | Defines URL to download the 'deb' package from for Debian/Ubuntu family systems.
duf_el_url        | Defines URL to download the 'rpm' package from for EL family systems.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **duf**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.duf
```

For customizing behavior of role (i.e. specifying the desired **duf** version) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.duf
  vars:
    duf_version: 0.6.1
```

For customizing behavior of role (i.e. different os architecture of **duf** package like arm64) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.duf
  vars:
    duf_arch: "arm64"
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-duf/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev)
