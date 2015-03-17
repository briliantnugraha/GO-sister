/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rmiserver;

import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import rmiserver.rmi.Pesan;

/**
 *
 * @author Peni Sriwahyu
 */
public class RMIServer {
    private void SrvReady() throws RemoteException{
        try{
            Registry registry = LocateRegistry.createRegistry(5050);
            registry.rebind("Echo", new Pesan());
        }
        catch(Exception e){
            System.out.println(e.getMessage());
        }
        System.out.println("Server is ready");
    }
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws RemoteException {
        RMIServer rm = new RMIServer();
        rm.SrvReady();
    }
    
}
