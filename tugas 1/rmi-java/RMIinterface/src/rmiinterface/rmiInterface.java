/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rmiinterface;

import java.awt.image.BufferedImage;
import java.io.IOException;
import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.ArrayList;

/**
 *
 * @author Peni Sriwahyu
 */
public interface rmiInterface extends Remote{
    String str (String name)throws RemoteException;
    byte[] bufferByte ( byte [] a) throws RemoteException, IOException;
    ArrayList arlist(ArrayList<byte []> byteFile, ArrayList<String> extFile) throws RemoteException, IOException;
}
