module com.main {
    requires javafx.controls;
    requires javafx.fxml;
    requires javafx.base;
    requires java.desktop;
    requires javafx.swing;

    opens com.main to javafx.fxml;
    exports com.main;
}
