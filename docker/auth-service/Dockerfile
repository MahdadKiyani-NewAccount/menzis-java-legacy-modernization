FROM openjdk:17-slim
WORKDIR /app
COPY AuthService.java .
RUN echo 'public class Runner { public static void main(String[] args) { System.out.println("Auth service running..."); } }' > Runner.java
RUN javac AuthService.java Runner.java
CMD ["java", "Runner"]

