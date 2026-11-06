from scapy.all import sniff, IP, TCP, UDP
import pandas as pd
import time 
import networkx as nx


packets_data_tabular = []
packets_data_graph = nx.DiGraph()

def process_packet(packet):
    if IP in packet:
        payload_len = len(packet[IP].payload)
        packet_info_tabular = {
            "timestamp": time.time(),
            "src_ip": packet[IP].src,
            "dst_ip": packet[IP].dst,
            "protocol": packet[IP].proto,
            "length": len(packet),
            "payload_length": payload_len
        }
        packets_data_tabular.append(packet_info_tabular)

        # add new entry to adjacency list (u -> v)
        src = packet[IP].src
        dst = packet[IP].dst

        add_vertex_to_graph(packets_data_graph, src)
        add_vertex_to_graph(packets_data_graph, dst)
        add_edge_to_graph(packets_data_graph, src, dst)
        # print(f"Packet captured: {packet_info_tabular}")
        print(f"Current adjacency list: {packets_data_graph}")

def add_edge_to_graph(graph: nx.Graph, src: str, dst: str):
    if not graph.has_edge(src, dst):
        graph.add_edge(src,dst, weight=1)
    else:
        graph[src][dst]['weight'] += 1

def add_vertex_to_graph(graph: nx.Graph, vertex: str):
    if not graph.has_node(vertex):
        graph.add_node(vertex)

def cleanup():
    # Perform any necessary cleanup actions here
    print("Cleaning up resources...")
    # clean table
    df = pd.DataFrame(packets_data_tabular)
    df.to_csv("packets_data.csv", index=False)

    # clean graph
    nx.write_gexf(packets_data_graph, "packets_graph.gexf")
    print("Packet data saved to packets_data.csv")

print("Starting packet capture... Press Ctrl+C to stop.")
try:
    sniff(iface='en1', prn=process_packet, count=1000, store=False)
    cleanup()
except KeyboardInterrupt:
    print("\nPacket capture stopped.")
    cleanup()


