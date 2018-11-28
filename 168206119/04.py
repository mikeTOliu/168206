class map_:
    graph = {}
    graph["yu_pu"] = {}
    graph["yu_pu"]["chang_pian"] = 5
    graph["yu_pu"]["hai_bao"] = 0
    graph["chang_pian"] = {}
    graph["chang_pian"]["ji_ta"] = 15
    graph["chang_pian"]["jia_zi_gu"] = 20
    graph["hai_bao"] = {}
    graph["hai_bao"]["ji_ta"] = 30
    graph["hai_bao"]["jia_zi_gu"] = 35
    graph["ji_ta"] = {}
    graph["ji_ta"]["gang_qing"] = 20
    graph["jia_zi_gu"] = {}
    graph["jia_zi_gu"]["gang_qing"] = 10
    graph["gang_qing"] = {}
    infinity = float("inf")
    costs = {}
    costs["chang_pian"] = 5
    costs["hai_bao"] = 0
    costs["ji_ta"] = infinity
    costs["jia_zi_gu"] = infinity 
    costs["gang_qing"] = infinity  
    parents = {}
    parents["chang_pian"] = "yu_pu"
    parents["hai_bao"] = "yu_pu"
    parents["ji_ta"] = None
    parents["jia_zi_gu"] = None
    parents["gang_qing"] = None
processed = [] 
# find lowest node
def find_lowest_cost_node(costs):	
    lowest_cost = float('inf')
    lowest_cost_node = None	
    for node in costs:			
        if not node in processed:				
            if costs[node] < lowest_cost:				
                lowest_cost = costs[node]				
                lowest_cost_node = node	
    return lowest_cost_node 
#find shurt  
def find_shortest_path():	
    node = "gang_qing"	
    shortest_path = ["gang_qing"]	
    while map_.parents[node] != "yu_pu":		
        shortest_path.append(map_.parents[node])		
        node = map_.parents[node]	
    shortest_path.append("yu_pu")	
    return shortest_path

def find_():	
    node = find_lowest_cost_node(map_.costs)	
    while node is not None:				
        cost =map_.costs[node]			
        neighbors =map_. graph[node]			
        for n in neighbors :			
	
            new_cost = cost + neighbors[n]			
            if new_cost <map_. costs[n]:				
                map_.costs[n] = new_cost				
                map_.parents[n] = node		
        print(node)
        processed.append(node)		
        node = find_lowest_cost_node(map_.costs)	
    shortest_path = find_shortest_path()	
    shortest_path.reverse()	
    print(shortest_path)		
find_()