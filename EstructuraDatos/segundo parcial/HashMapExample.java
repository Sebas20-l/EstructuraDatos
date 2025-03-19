import java.util.HashMap;

public class HashMapExample {
    private HashMap<String, String> capitalCities;

    // Constructor
    public HashMapExample() {
        capitalCities = new HashMap<>();
        capitalCities.put("England", "London");
        capitalCities.put("Germany", "Berlin");
        capitalCities.put("Norway", "Oslo");
        capitalCities.put("USA", "Washington DC");
    }

    // Método para obtener la capital de un país
    public String obtenerCapital(String pais) {
        return capitalCities.getOrDefault(pais, "No encontrado");
    }

    // Método para mostrar todas las capitales
    public void mostrarCapitales() {
        for (String country : capitalCities.keySet()) {
            System.out.println("País: " + country + ", Capital: " + capitalCities.get(country));
        }
    }
}

