import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.PrintStream;
import java.io.IOException;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.ArrayList;

public class Client {
  public static void main(String[] args) {

    Socket clientSocket = null;
    BufferedReader is = null;
    PrintStream os = null;
    BufferedReader inputLine = null;

    /*
     * Open a socket on port 2222. Open the input and the output streams.
     */
    try 
    {
        clientSocket = new Socket("localhost", 2222);
        os = new PrintStream(clientSocket.getOutputStream());
        is = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
        System.out.println(is.readLine());
        System.out.println(is.readLine());
        inputLine = new BufferedReader(new InputStreamReader(System.in));
    } 
    catch (UnknownHostException e) 
    {
      System.err.println("Don't know about host");
    } 
    catch (IOException e) 
    {
      System.err.println("Couldn't get I/O for the connection to host");
    }

    /*
     * If everything has been initialized then we want to write some data to the
     * socket we have opened a connection to on port 2222.
     */
    while(true)
    {
      try 
      {

        /*
         * Keep on reading from/to the socket till we receive the "EXIT" from the
         * server, once we received that then we break.
         */
        System.out.println("Select: UPPERCASE, LOWERCASE, GET REVERSE, or EXIT");
        String responseLine;
        String checker = inputLine.readLine();
        os.println(checker);
        if((responseLine = is.readLine()) != null)
        {
          System.out.println(responseLine);
          if(checker.equals("UPPERCASE") && responseLine.equals("200 OK")) 
          {
        	  ArrayList<String> words = new ArrayList<String>();
        	  System.out.println("Type a word(s) to be Uppercased:");
        	  while(true)
        	  {
            	  String input = inputLine.readLine();
            	  if(input.equals("."))
            	  {
            		  words.add(input);
            		  for(String x: words)
            		  {
            			  os.println(x);
            			  if(!x.equals("."))
            			  {
            				  responseLine = is.readLine();
                        	  System.out.println(responseLine);
            			  }
            		  }
            		  break;
            	  }
            	  else
            	  {
            		  words.add(input);
            	  }
        	  }
          }
          else if(checker.equals("LOWERCASE") && responseLine.equals("200 OK")) 
          {
        	  ArrayList<String> words = new ArrayList<String>();
        	  System.out.println("Type a word(s) to be Lowercased:");
        	  while(true)
        	  {
            	  String input = inputLine.readLine();
            	  if(input.equals("."))
            	  {
            		  words.add(input);
            		  for(String x: words)
            		  {
            			  os.println(x);
            			  if(!x.equals("."))
            			  {
            				  responseLine = is.readLine();
                        	  System.out.println(responseLine);
            			  }
            		  }
            		  break;
            	  }
            	  else
            	  {
            		  words.add(input);
            	  }
        	  }
          }
          else if(checker.equals("REVERSE") && responseLine.equals("200 OK"))
          {
        	  System.out.println("Type a word to be Reversed: ");
        	  os.println(inputLine.readLine());
        	  responseLine = is.readLine();
        	  System.out.println(responseLine);
          }
          else if (checker.equals("EXIT") && responseLine.equals("200 OK")) 
          {
        	  os.close();
              is.close();
              clientSocket.close();
              break;
          }
        }

        /*
         * Close the output stream, close the input stream, close the socket.
         */
        
      } catch (UnknownHostException e) {
        System.err.println("Trying to connect to unknown host: " + e);
      } catch (IOException e) {
        System.err.println("IOException:  " + e);
      }
    }
  }
}