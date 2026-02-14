# Spring Boot Structuring Code

- URL: https://docs.spring.io/spring-boot/reference/using/structuring-your-code.html
- Retrieved: 2026-02-14 12:32:14 UTC
- Partition: `backend`
- Fetch status: `ok`

## Distilled Key Point

- Use consistent package structure and explicit layer boundaries.

## Extracted Source Snapshot

```text
Structuring Your Code :: Spring Boot

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

Spring Boot
4.0.2

Search

Overview

Documentation

Community

System Requirements

Installing Spring Boot

Upgrading Spring Boot

Tutorials

Developing Your First Spring Boot Application

Reference

Developing with Spring Boot

Build Systems

Structuring Your Code

Configuration Classes

Auto-configuration

Spring Beans and Dependency Injection

Using the @SpringBootApplication Annotation

Running Your Application

Developer Tools

Packaging Your Application for Production

Core Features

SpringApplication

Externalized Configuration

Profiles

Logging

Internationalization

Aspect-Oriented Programming

JSON

Task Execution and Scheduling

Development-time Services

Creating Your Own Auto-configuration

Kotlin Support

SSL

Web

Servlet Web Applications

Reactive Web Applications

Graceful Shutdown

Spring Security

Spring Session

Spring for GraphQL

Spring HATEOAS

Data

SQL Databases

Working with NoSQL Technologies

IO

Caching

Spring Batch

Hazelcast

Quartz Scheduler

Sending Email

Validation

Calling REST Services

Web Services

Distributed Transactions With JTA

Messaging

JMS

AMQP

Apache Kafka Support

Apache Pulsar Support

RSocket

Spring Integration

WebSockets

Testing

Test Modules

Test Scope Dependencies

Testing Spring Applications

Testing Spring Boot Applications

Testcontainers

Test Utilities

Packaging Spring Boot Applications

Efficient Deployments

AOT Cache

Ahead-of-Time Processing With the JVM

GraalVM Native Images

Introducing GraalVM Native Images

Advanced Native Images Topics

Checkpoint and Restore With the JVM

Container Images

Efficient Container Images

Dockerfiles

Cloud Native Buildpacks

Production-ready Features

Enabling Production-ready Features

Endpoints

Monitoring and Management Over HTTP

Monitoring and Management over JMX

Observability

Loggers

Metrics

Tracing

Auditing

Recording HTTP Exchanges

Process Monitoring

Cloud Foundry Support

How-to Guides

Spring Boot Application

Properties and Configuration

Embedded Web Servers

Spring MVC

Jersey

HTTP Clients

Logging

Data Access

Database Initialization

NoSQL

Messaging

Batch Applications

Actuator

Security

Hot Swapping

Testing

Build

Ahead-of-Time Processing

GraalVM Native Applications

Developing Your First GraalVM Native Application

Testing GraalVM Native Images

AOT Cache

Deploying Spring Boot Applications

Traditional Deployment

Deploying to the Cloud

Installing Spring Boot Applications

Docker Compose

Build Tool Plugins

Maven Plugin

Getting Started

Using the Plugin

Goals

Packaging Executable Archives

Packaging OCI Images

Running your Application with Maven

Ahead-of-Time Processing

Running Integration Tests

Integrating with Actuator

Help Information

Gradle Plugin

Getting Started

Managing Dependencies

Packaging Executable Archives

Packaging OCI Images

Publishing your Application

Running your Application with Gradle

Ahead-of-Time Processing

Integrating with Actuator

Reacting to Other Plugins

Spring Boot AntLib Module

Supporting Other Build Systems

Spring Boot CLI

Installing the CLI

Using the CLI

Rest APIs

Actuator

Audit Events ( auditevents
)

Beans ( beans
)

Caches ( caches
)

Conditions Evaluation Report ( conditions
)

Configuration Properties ( configprops
)

Environment ( env
)

Flyway ( flyway
)

Health ( health
)

Heap Dump ( heapdump
)

HTTP Exchanges ( httpexchanges
)

Info ( info
)

Spring Integration Graph ( integrationgraph
)

Liquibase ( liquibase
)

Log File ( logfile
)

Loggers ( loggers
)

Mappings ( mappings
)

Metrics ( metrics
)

Prometheus ( prometheus
)

Quartz ( quartz
)

Software Bill of Materials ( sbom
)

Scheduled Tasks ( scheduledtasks
)

Sessions ( sessions
)

Shutdown ( shutdown
)

Application Startup ( startup
)

Thread Dump ( threaddump
)

Java APIs

Spring Boot

Gradle Plugin

Maven Plugin

Kotlin APIs

Spring Boot

Specifications

Configuration Metadata

Metadata Format

Providing Manual Hints

Generating Your Own Metadata by Using the Annotation Processor

The Executable Jar Format

Nested JARs

Spring Boot’s “NestedJarFile” Class

Launching Executable Jars

PropertiesLauncher Features

Executable Jar Restrictions

Alternative Single Jar Solutions

Appendix

Common Application Properties

Deprecated Application Properties

Auto-configuration Classes

spring-boot-activemq

spring-boot-actuator-autoconfigure

spring-boot-amqp

spring-boot-artemis

spring-boot-autoconfigure

spring-boot-batch

spring-boot-batch-jdbc

spring-boot-cache

spring-boot-cassandra

spring-boot-cloudfoundry

spring-boot-couchbase

spring-boot-data-cassandra

spring-boot-data-commons

spring-boot-data-couchbase

spring-boot-data-elasticsearch

spring-boot-data-jdbc

spring-boot-data-jpa

spring-boot-data-ldap

spring-boot-data-mongodb

spring-boot-data-neo4j

spring-boot-data-r2dbc

spring-boot-data-redis

spring-boot-data-rest

spring-boot-devtools

spring-boot-elasticsearch

spring-boot-flyway

spring-boot-freemarker

spring-boot-graphql

spring-boot-groovy-templates

spring-boot-gson

spring-boot-h2console

spring-boot-hateoas

spring-boot-hazelcast

spring-boot-health

spring-boot-hibernate

spring-boot-http-client

spring-boot-http-codec

spring-boot-http-converter

spring-boot-integration

spring-boot-jackson

spring-boot-jackson2

spring-boot-jdbc

spring-boot-jersey

spring-boot-jetty

spring-boot-jms

spring-boot-jooq

spring-boot-jsonb

spring-boot-kafka

spring-boot-kotlinx-serialization-json

spring-boot-ldap

spring-boot-liquibase

spring-boot-mail

spring-boot-micrometer-metrics

spring-boot-micrometer-observation

spring-boot-micrometer-tracing

spring-boot-micrometer-tracing-brave

spring-boot-micrometer-tracing-opentelemetry

spring-boot-mongodb

spring-boot-mustache

spring-boot-neo4j

spring-boot-netty

spring-boot-opentelemetry

spring-boot-persistence

spring-boot-pulsar

spring-boot-quartz

spring-boot-r2dbc

spring-boot-reactor

spring-boot-reactor-netty

spring-boot-restclient

spring-boot-resttestclient

spring-boot-rsocket

spring-boot-security

spring-boot-security-oauth2-authorization-server

spring-boot-security-oauth2-client

spring-boot-security-oauth2-resource-server

spring-boot-security-saml2

spring-boot-sendgrid

spring-boot-servlet

spring-boot-session

spring-boot-session-data-redis

spring-boot-session-jdbc

spring-boot-testcontainers

spring-boot-thymeleaf

spring-boot-tomcat

spring-boot-transaction

spring-boot-validation

spring-boot-webclient

spring-boot-webflux

spring-boot-webmvc

spring-boot-webservices

spring-boot-websocket

spring-boot-zipkin

Test Auto-configuration Annotations

Test Slices

Dependency Versions

Managed Dependency Coordinates

Version Properties

Search

Edit this Page

GitHub Project

Stack Overflow

Spring Boot

Reference

Developing with Spring Boot

Structuring Your Code

Structuring Your Code

Spring Boot does not require any specific code layout to work.
However, there are some best practices that help.

If you wish to enforce a structure based on domains, take a look at  Spring Modulith .

Using the “default” Package

When a class does not include a  package
declaration, it is considered to be in the “default package”.
The use of the “default package” is generally discouraged and should be avoided.
It can cause particular problems for Spring Boot applications that use the   @ComponentScan
,   @ConfigurationPropertiesScan
,   @EntityScan
, or   @SpringBootApplication
annotations, since every class from every jar is read.

We recommend that you follow Java’s recommended package naming conventions and use a reversed domain name (for example,  com.example.project
).

Locating the Main Application Class

We generally recommend that you locate your main application class in a root package above other classes.
The   @SpringBootApplication
annotation  is often placed on your main class, and it implicitly defines a base “search package” for certain items.
For example, if you are writing a JPA application, the package of the   @SpringBootApplication
annotated class is used to search for   @Entity
items.
Using a root package also allows component scan to apply only on your project.

If you do not want to use   @SpringBootApplication
, the   @EnableAutoConfiguration
and   @ComponentScan
annotations that it imports defines that behavior so you can also use those instead.

The following listing shows a typical layout:

com
+- example
+- myapplication
+- MyApplication.java
|
+- customer
|   +- Customer.java
|   +- CustomerController.java
|   +- CustomerService.java
|   +- CustomerRepository.java
|
+- order
+- Order.java
+- OrderController.java
+- OrderService.java
+- OrderRepository.java

The  MyApplication.java
file would declare the  main
method, along with the basic   @SpringBootApplication
, as follows:

Java

Kotlin

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MyApplication {

public static void main(String[] args) {
SpringApplication.run(MyApplication.class, args);
}

}

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class MyApplication

fun main(args: Array<String>) {
runApplication<MyApplication>(*args)
}

Build Systems
Configuration Classes

Spring Boot

Stable

4.0.2

3.5.10

3.4.13

3.3.13

Preview

4.1.0-M1

Snapshot

4.1.0-SNAPSHOT

4.0.3-SNAPSHOT

3.5.11-SNAPSHOT

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
