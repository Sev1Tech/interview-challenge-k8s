FROM gradle:5.4-jdk11 as build

USER root
WORKDIR /app
COPY ./ /app/
RUN gradle build -x test --no-daemon --console plain

FROM openjdk:11.0-jdk

WORKDIR /app
COPY --from=build /app/build/libs/person-service-0.0.1-SNAPSHOT.jar /app/app.jar
CMD ["java", "-Djava.security.egd=file:/dev/./urandom", "-jar", "/app/app.jar"]
