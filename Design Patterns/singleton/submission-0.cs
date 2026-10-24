public class Singleton {
    private static Singleton uniqueInstance = null;
    private string value = null;

    private Singleton() {

    }

    public static Singleton getInstance() {
        if (uniqueInstance is null) {
            uniqueInstance = new Singleton();
        }

        return uniqueInstance;
    }

    public string getValue() {
        return value;
    }

    public void setValue(string value){
        this.value = value;
    }
}
