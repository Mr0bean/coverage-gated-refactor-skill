# Spring Modulith Reference

- URL: https://docs.spring.io/spring-modulith/reference/
- Retrieved: 2026-02-14 12:32:18 UTC
- Partition: `backend`
- Fetch status: `ok`

## Distilled Key Point

- Use explicit module boundaries and events in modular monoliths.

## Extracted Source Snapshot

```text
Spring Modulith :: Spring Modulith

Why Spring

Overview
Microservices
Reactive
Event
Driven
Cloud
Web
Applications
Serverless
Batch

Learn

Overview
Quickstart
Guides
Blog

Projects

Overview
Spring Boot
Spring Framework
Spring Cloud
Spring Cloud Data Flow
Spring Data
Spring Integration
Spring Batch
Spring Security
View all projects
DEVELOPMENT TOOLS

Spring Tools 4
Spring Initializr

Academy

Courses
Get Certified

Solutions

Overview
Spring Runtime
Spring Consulting
Spring Academy For Teams
Security Advisories

Community

Overview
Events
Team

light

Spring Modulith
2.0.2

Search

Overview

Fundamentals

Verifying Application Module Structure

Working with Application Events

Integration Testing Application Modules

Moments — a Passage of Time Events API

Documenting Application Modules

Spring Modulith Runtime Support

Production-ready Features

Appendix

Search

Edit this Page

GitHub Project

Spring Modulith

Overview

Spring Modulith

© 2022-2025 The original authors.

Copies of this document may be made for your own use and for distribution to others, provided that you do not charge any fee for such copies and further provided that each copy contains this Copyright Notice, whether distributed in print or electronically.

Overview

Spring Modulith is an opinionated toolkit to build domain-driven, modular applications with Spring Boot.
In the same way that Spring Boot has an opinion on the technical arrangement of an application, Spring Modulith implements an opinion on how to structure an app functionally and allows its individual, logical parts to interact with each other.
As a result, Spring Modulith enables developers to build applications that are easier to update so they can accommodate changing business requirements over time.

Project Metadata

Version control  github.com/spring-projects/spring-modulith

Bug tracker:  github.com/spring-projects/spring-modulith

Release repository: Maven central

Milestone repository:  repo.spring.io/milestone

Snapshot repository:  repo.spring.io/snapshot

Javadoc:  docs.spring.io/spring-modulith/docs/2.0.2/api

Spring Boot compatibility

Find a full Spring Boot compatibility matrix  here .

Using Spring Modulith

Spring Modulith consists of a set of libraries that can be used individually and depending on which features of it you would like to use.
To ease the declaration of the individual modules, we recommend to declare the following BOM in your Maven POM:

Using the Spring Modulith BOM

Maven

Gradle

<dependencyManagement>
<dependencies>
<dependency>
<groupId>org.springframework.modulith</groupId>
<artifactId>spring-modulith-bom</artifactId>
<version>2.0.2</version>
<scope>import</scope>
<type>pom</type>
</dependency>
</dependencies>
</dependencyManagement>

dependencyManagement {
imports {
mavenBom 'org.springframework.modulith:spring-modulith-bom:2.0.2'
}
}

The individual sections describing Spring Modulith features will refer to the individual artifacts that are needed to make use of the feature.
For an overview about all modules available, have a look at  Spring Modulith modules .

Examples

If you would like to play with the features of the project and see them live in action, check out the examples  here

Fundamentals

Spring Modulith

Stable

2.0.2

1.4.7

1.3.12

1.2.13

1.1.12

Preview

2.1.0-M1

Snapshot

2.1.0-SNAPSHOT

2.0.3-SNAPSHOT

1.4.8-SNAPSHOT

1.3.13-SNAPSHOT

1.2.14-SNAPSHOT

1.1.13-SNAPSHOT

Related Spring Documentation

Spring Boot

Spring Framework

Spring Cloud

Spring Cloud Build

Spring Cloud Bus

Spring Cloud Circuit Breaker

Spring Cloud Commons

Spring Cloud Config

Spring Cloud Consul

Spring Cloud Contract

Spring Cloud Function

Spring Cloud Gateway

Spring Cloud Kubernetes

Spring Cloud Netflix

Spring Cloud OpenFeign

Spring Cloud Stream

Spring Cloud Task

Spring Cloud Vault

Spring Cloud Zookeeper

Spring Data

Spring Data Cassandra

Spring Data Commons

Spring Data Couchbase

Spring Data Elasticsearch

Spring Data JPA

Spring Data KeyValue

Spring Data LDAP

Spring Data MongoDB

Spring Data Neo4j

Spring Data Redis

Spring Data JDBC & R2DBC

Spring Data REST

Spring Integration

Spring Batch

Spring Security

Spring Authorization Server

Spring LDAP

Spring Security Kerberos

Spring Session

Spring Vault

Spring AI

Spring AMQP

Spring CLI

Spring GraphQL

Spring for Apache Kafka

Spring Modulith

Spring for Apache Pulsar

Spring Shell

All Docs...

Copyright © 2005 -   Broadcom. All Rights Reserved. The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.  Terms of Use  •  Privacy  •  Trademark Guidelines   •  Thank you   •  Your California Privacy Rights  •  Cookie Settings

Apache®, Apache Tomcat®, Apache Kafka®, Apache Cassandra™, and Apache Geode™ are trademarks or registered trademarks of the Apache Software Foundation in the United States and/or other countries. Java™, Java™ SE, Java™ EE, and OpenJDK™ are trademarks of Oracle and/or its affiliates. Kubernetes® is a registered trademark of the Linux Foundation in the United States and other countries. Linux® is the registered trademark of Linus Torvalds in the United States and other countries. Windows® and Microsoft® Azure are registered trademarks of Microsoft Corporation. “AWS” and “Amazon Web Services” are trademarks or registered trademarks of Amazon.com Inc. or its affiliates. All other trademarks and copyrights are property of their respective owners and are only mentioned for informative purposes. Other names may be trademarks of their respective owners.

Search in all Spring Docs
```
