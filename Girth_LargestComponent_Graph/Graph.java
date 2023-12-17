package Girth_LargestComponent_Graph;
// Graded Lab 2 b 
// Kartheek Kotha 2110110292 kk746
// L.Gnanesh Chowdary, 2110110307,lc607
// Guru Charan, 2110110084 ,ac271



import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class Graph {
    // Representation of the graph using adjacency list
    // Representation of the graph using adjacency list
    private Map<Integer, List<Integer>> adjacencyList = new HashMap<>();

    // Number of nodes in the graph
    private int numNodes;

    // Number of edges in the graph
    private int numEdges;

    private void readGraphFromFile(String filePath) {
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            boolean isHeader = true;
    
            while ((line = br.readLine()) != null) {
                if (isHeader) {
                    if (line.startsWith("# Nodes:")) {
                        String[] headerParts = line.split("\\s+");
                        numNodes = Integer.parseInt(headerParts[2]);
                        numEdges = Integer.parseInt(headerParts[4]);
                        initializeGraph(numNodes);
                        isHeader = false;
                    }
                } else if (!line.startsWith("#")) {
                    String[] nodes = line.split("\\s+");  // Split on any whitespace
                    int fromNodeId = Integer.parseInt(nodes[0]);
                    int toNodeId = Integer.parseInt(nodes[1]);
    
                    addEdge(fromNodeId, toNodeId);
                }
            }
            System.err.println("Number of nodes and edges are : " + numNodes + " " + numEdges);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }


    // Method to initialize the graph with given number of nodes
    private void initializeGraph(int numNodes) {
        for (int i = 0; i < numNodes; i++) {
            adjacencyList.put(i, new ArrayList<>());
        }
    }

    // Method to add an edge to the graph
    private void addEdge(int fromNodeId, int toNodeId) {
        if (!adjacencyList.get(fromNodeId).contains(toNodeId)) {
            adjacencyList.get(fromNodeId).add(toNodeId);
        }
        if (!adjacencyList.get(toNodeId).contains(fromNodeId)) {
            adjacencyList.get(toNodeId).add(fromNodeId);
        }
    }

    private void findLargestConnectedComponent() {
        Set<Integer> visited = new HashSet<>();
        int maxSize = 0;

        for (int node : adjacencyList.keySet()) {
            if (!visited.contains(node)) {
                Set<Integer> connectedComponent = new HashSet<>();
                dfs(node, visited, connectedComponent);

                if (connectedComponent.size() > maxSize) {
                    maxSize = connectedComponent.size();
                }
            }
        }

        System.out.println("Largest Connected Component Size using dfs is : " + maxSize);
    }

    private void dfs(int node, Set<Integer> visited, Set<Integer> connectedComponent) {
        visited.add(node);
        connectedComponent.add(node);

        for (int neighbor : adjacencyList.get(node)) {
            if (!visited.contains(neighbor)) {
                dfs(neighbor, visited, connectedComponent);
            }
        }
    }

       // Method to find the girth of the graph using BFS
    private int findGirthBFS() {
        int minCycleLength = Integer.MAX_VALUE;

        for (int node : adjacencyList.keySet()) {
            int cycleLength = findCycleLengthBFS(node);
            if (cycleLength != -1 && cycleLength < minCycleLength) {
                minCycleLength = cycleLength;
            }
        }

        return (minCycleLength == Integer.MAX_VALUE) ? -1 : minCycleLength;
    }

    private int findCycleLengthBFS(int startNode) {
        Queue<Integer> queue = new LinkedList<>();
        Map<Integer, Integer> distance = new HashMap<>();

        queue.add(startNode);
        distance.put(startNode, 0);

        while (!queue.isEmpty()) {
            int currentNode = queue.poll();

            for (int neighbor : adjacencyList.get(currentNode)) {
                if (!distance.containsKey(neighbor)) {
                    distance.put(neighbor, distance.get(currentNode) + 1);
                    queue.add(neighbor);
                } else if (neighbor != currentNode && distance.get(neighbor) < distance.get(currentNode)) {
                    // Found a cycle
                    return distance.get(currentNode) + distance.get(neighbor) + 1;
                }
            }
        }

        return -1; // No cycle found
    }

    public static void main(String[] args) {
        Graph graphOperations = new Graph();
        // graphOperations.readGraphFromFile("test.txt");
        graphOperations.readGraphFromFile("Email-Enron.txt");

        graphOperations.findLargestConnectedComponent();

        int girth = graphOperations.findGirthBFS();
        if (girth == -1) {
            System.out.println("Graph is acyclic");
        } else {
            System.out.println("Girth of the graph using bfs is : " + girth);
        }
    }
}
