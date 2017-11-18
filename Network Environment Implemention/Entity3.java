public class Entity3 extends Entity
{    
    // Perform any necessary initialization in the constructor
    public Entity3()
    {
    	for(int i = 0; i < NetworkSimulator.NUMENTITIES; i++)
    	{
    		for(int j = 0; j < NetworkSimulator.NUMENTITIES; j++)
    		{
    			if (i == 3 || i == j)
    			{
    				distanceTable[i][j] = NetworkSimulator.cost[i][j];
    			}
    			else
    			{
    				distanceTable[i][j] = 999;
    			}
    		}
    	}
    	
    	printDT();
    	
    	for(int i = 0; i < NetworkSimulator.NUMENTITIES; i++)
    	{
    		if (i != 3)
    		{
    			if (NetworkSimulator.cost[3][i] != 999)
    			{
    				int[] copy = new int[NetworkSimulator.NUMENTITIES];
    				for(int x = 0; x < NetworkSimulator.NUMENTITIES; x++)
    				{
    					copy[x] = distanceTable[3][x];
    				}
    				
    				Packet p = new Packet(3, i, copy);
    				NetworkSimulator.toLayer2(p);
    			}
    		}
    	}
    }
    
    // Handle updates when a packet is received.  Students will need to call
    // NetworkSimulator.toLayer2() with new packets based upon what they
    // send to update.  Be careful to construct the source and destination of
    // the packet correctly.  Read the warning in NetworkSimulator.java for more
    // details.
    public void update(Packet p)
    {
    	System.out.println("------------------------------------");
    	System.out.println("The beginning of update() in node " + String.valueOf(p.getDest()));
    	System.out.println("------------------------------------");
    	System.out.println();
    	printDT();
    	
    	for(int i = 0; i < NetworkSimulator.NUMENTITIES; i++)
    	{
    		distanceTable[p.getSource()][i] = p.getMincost(i);
    	}
    	
    	int cost = 0;
        boolean changed = false;
    	for(int x = 0; x < NetworkSimulator.NUMENTITIES; x++)
    	{
    		for(int y = 0; y < NetworkSimulator.NUMENTITIES; y++)
    		{
    			cost = distanceTable[x][y];
    			
    			if(x != 3)
    			{
    				cost += distanceTable[3][x];
    			}
    			
    			if(cost < NetworkSimulator.cost[3][y])
    			{
    				NetworkSimulator.cost[3][y] = cost;
    			    changed = true;
    			}
    		}
    	}
    	
    	System.out.println("------------------------------------");
    	System.out.println("The end of update() in node " + String.valueOf(p.getDest()));
    	System.out.println("------------------------------------");
    	System.out.println();
    	
    	if(changed)
    	{
    		printDT();
    		System.out.println("Distance Vector Updated!");
    		for(int i = 0; i < NetworkSimulator.NUMENTITIES; i++)
        	{
        		if (i != 3)
        		{
        			if (NetworkSimulator.cost[3][i] != 999)
        			{
        				int[] copy = new int[NetworkSimulator.NUMENTITIES];
        				for(int x = 0; x < NetworkSimulator.NUMENTITIES; x++)
        				{
        					copy[x] = distanceTable[3][x];
        				}
        				
        				Packet k = new Packet(3, i, copy);
        				NetworkSimulator.toLayer2(k);
        			}
        		}
        	}
    	}
    	else
    	{
    		printDT();
    		System.out.println("No change!!");
    	}
    }
    
    public void linkCostChangeHandler(int whichLink, int newCost)
    {
    }
    
 public void printDT()
       {
           System.out.println();
           System.out.println("           via");
           System.out.println(" D3 |  0   1   2   3");
           System.out.println("----+-----------------");
           for (int i = 0; i < NetworkSimulator.NUMENTITIES; i++)
           {
               System.out.print("   " + i + "|");
               for (int j = 0; j < NetworkSimulator.NUMENTITIES; j++)
               {
                   if (distanceTable[i][j] < 10)
                   {
                       System.out.print("   ");
                   }
                   else if (distanceTable[i][j] < 100)
                   {
                       System.out.print("  ");
                   }
                   else
                   {
                       System.out.print(" ");
                   }

                   System.out.print(distanceTable[i][j]);
               }
               System.out.println();
           }
    }
}