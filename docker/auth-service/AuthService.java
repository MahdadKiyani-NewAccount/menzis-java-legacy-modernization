public class AuthService {
    public String login(String user, String pass) {
        // Placeholder auth logic
        return user.equals("admin") ? "token123" : "unauthorized";
    }
}

