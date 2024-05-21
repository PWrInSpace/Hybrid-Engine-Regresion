package com.main;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.chart.LineChart;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.scene.chart.XYChart;
import javafx.scene.control.ListView;
import javafx.scene.control.SplitPane;
import javafx.embed.swing.SwingFXUtils;
import javafx.scene.SnapshotParameters;
import javafx.scene.image.WritableImage;
import javax.imageio.ImageIO;
import java.io.File;
import java.io.IOException;
import javafx.application.Platform;

public class Controller {

    @FXML
    private LineChart<Number, Number> Graph;

    @FXML
    private ListView<String> ListOperationObjects;

    @FXML
    private SplitPane MainSplitPane;

    @FXML
    void initialize() {
        // Add items to the ListView
        ListOperationObjects.getItems().addAll("Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9", "Item 10");
    }

    @FXML
    private Font x1;

    @FXML
    private Color x2;

    @FXML
    private Font x3;

    @FXML
    private Color x4;

    @FXML
    void ButtonAction(ActionEvent event) {
        // Set the title and axis labels
        Graph.setTitle("Test");
        Graph.getXAxis().setLabel("Time[s]");
        Graph.getYAxis().setLabel("Force[N]");
    
        // Create the first series
        XYChart.Series<Number, Number> series1 = new XYChart.Series<>();
        series1.setName("Series 1");
        series1.getData().add(new XYChart.Data<>(0, 0));
        series1.getData().add(new XYChart.Data<>(1, 2));
        series1.getData().add(new XYChart.Data<>(2, 1));
    
        // Create the second series
        XYChart.Series<Number, Number> series2 = new XYChart.Series<>();
        series2.setName("Series 2");
        series2.getData().add(new XYChart.Data<>(0, 1));
        series2.getData().add(new XYChart.Data<>(1, 3));
        series2.getData().add(new XYChart.Data<>(2, 2));
    
        // Add the series to the chart
        Graph.getData().addAll(series1, series2);
    
        // Take a snapshot of the LineChart
        WritableImage image = Graph.snapshot(new SnapshotParameters(), null);
    
        // Write the snapshot to a file
        File file = new File("chart.png");
        try {
            ImageIO.write(SwingFXUtils.fromFXImage(image, null), "png", file);
        } catch (IOException e) {
            // Handle exception
            e.printStackTrace();
        }
    }


}
