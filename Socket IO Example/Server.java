import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.io.IOException;
import java.net.Socket;
import java.net.ServerSocket;

public class Server 
{
	
  public static void main(String args[]) 
  {
	  
    ServerSocket echoServer = null;
    String line;
    BufferedReader is;
    //DataInputStream is;
    PrintStream os;
    Socket clientSocket = null;

   
    try 
    {
    	echoServer = new ServerSocket(2222);
    }
    catch (IOException e) 
    {
    	System.out.println(e);
    }

    /*
     * Create a socket object from the ServerSocket to listen to and accept
     * connections. Open input and output streams.
     */
    System.out.println("The server started. To stop it press <CTRL><C>.");
    
    try 
    {
      clientSocket = echoServer.accept();
      //is = new DataInputStream(clientSocket.getInputStream());
      is = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
      os = new PrintStream(clientSocket.getOutputStream());
      os.println("server: got connection from client " + clientSocket.getRemoteSocketAddress());
      os.println("Server is Ready...");

      /* As long as we receive data, echo that data back to the client. */
      while(true) 
      {
       line = is.readLine();
       if(line.equals("UPPERCASE")) 
       {
           os.println("200 OK");
           System.out.println(clientSocket.getRemoteSocketAddress() + " sends UPPERCASE");
           while(true)
           {
        	   line = is.readLine();
               if(!line.equals("."))
               {
            	   os.println("From server: " + line.toUpperCase());
               }
               else
               {
            	   break;
               }
           }
       }
       else if(line.equals("LOWERCASE"))
       {
    	   os.println("200 OK");
    	   System.out.println(clientSocket.getRemoteSocketAddress() + " sends LOWERCASE");
           while(true)
           {
        	   line = is.readLine();
               if(!line.equals("."))
               {
            	   os.println("From server: " + line.toLowerCase());
               }
               else
               {
            	   break;
               }
           }
       }
       else if(line.equals("REVERSE"))
       {
    	   os.println("200 OK");
    	   System.out.println(clientSocket.getRemoteSocketAddress() + " sends REVERSE");
           
           line = new StringBuilder(is.readLine()).reverse().toString();
           os.println("From server: " + line.toLowerCase());
       }
       else if(line.equals("EXIT"))
       {
    	   os.println("200 OK");
    	   System.out.println(clientSocket.getRemoteSocketAddress() + " sends EXIT");
    	   os.close();
           is.close();
           echoServer.close();
           break;
       }
       
       else
       {
    	   os.println("400: Not a valid command!");
       }
      }
    }
    catch (IOException e) 
    {
      System.out.println(e);
    }
  }
}