package com.mingeso.backend.repositories;

import org.springframework.beans.factory.annotation.*;
import org.springframework.context.annotation.*;
import org.sql2o.*;

@Configuration
public class DatabaseContext {
    @Value("${database.url}")
    private String dbUrl;

    @Value("${database.user}")
    private String dbUser;

    @Value("${database.password}")
    private String dbPassword;

    @Bean
    public Sql2o sql2o() {
        return new Sql2o(dbUrl, dbUser, dbPassword);
    }
}
