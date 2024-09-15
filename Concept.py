// Vehicle Adjustment for Road Conditions

// Define a class to represent a vehicle
class Vehicle {
    String make;
    String model;
    int year;
    String currentRoadType;

    // Constructor
    Vehicle(String make, String model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;
        this.currentRoadType = "Standard";
    }

    // Method to adjust the vehicle for different road types
    void adjustForRoad(String roadType) {
        switch (roadType) {
            case "Highway":
                adjustSuspension("Soft");
                adjustTirePressure("High");
                adjustEngineMapping("Economy");
                break;
            case "City":
                adjustSuspension("Medium");
                adjustTirePressure("Medium");
                adjustEngineMapping("Balanced");
                break;
            case "OffRoad":
                adjustSuspension("Hard");
                adjustTirePressure("Low");
                adjustEngineMapping("Performance");
                break;
            default:
                adjustSuspension("Standard");
                adjustTirePressure("Standard");
                adjustEngineMapping("Standard");
        }
        this.currentRoadType = roadType;
    }

    // Simulated methods for adjustments (details would depend on vehicle's specific systems and capabilities)
    void adjustSuspension(String setting) {
        // Logic to adjust suspension
        System.out.println("Suspension adjusted to " + setting);
    }

    void adjustTirePressure(String pressure) {
        // Logic to adjust tire pressure
        System.out.println("Tire pressure adjusted to " + pressure);
    }

    void adjustEngineMapping(String mapping) {
        // Logic to adjust engine mapping
        System.out.println("Engine mapping adjusted to " + mapping);
    }
}

// Main class to demonstrate the functionality
public class RoadAdjustmentDemo {
    public static void main(String[] args) {
        // Create a vehicle instance
        Vehicle myVehicle = new Vehicle("Tesla", "Model S", 2020);

        // Adjust the vehicle for different road types
        myVehicle.adjustForRoad("Highway");
        myVehicle.adjustForRoad("City");
        myVehicle.adjustForRoad("OffRoad");
    }
}
