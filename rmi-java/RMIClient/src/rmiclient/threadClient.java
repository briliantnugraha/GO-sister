/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rmiclient;

import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.imageio.ImageIO;
import static rmiclient.RMIClient.FOLDER_PATH_SOURCE;
import rmiinterface.rmiInterface;

/**
 *
 * @author Peni Sriwahyu
 */
public class threadClient extends Thread{
    
    String ipServer;
    int id;
    public threadClient(String ipServer, int id){
        this.ipServer = ipServer;
        this.id = id;
    }
    
    @Override
    public void run(){
        try {
            bacaFile();
        } catch (IOException ex) {
            Logger.getLogger(threadClient.class.getName()).log(Level.SEVERE, null, ex);
        } catch (NotBoundException ex) {
            Logger.getLogger(threadClient.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
     private void bacaFile() throws FileNotFoundException, IOException, RemoteException, NotBoundException{
    /*untuk menyambungkan client dengan server - getRegistry*/
        Registry reg = LocateRegistry.getRegistry(this.ipServer, 5050);
        rmiInterface rm = (rmiInterface) reg.lookup("Echo");
       
    /*mengambil list file dan extensi dan membuat byte array file image*/
        File folder = new File(FOLDER_PATH_SOURCE);
        File[] listOfFiles = folder.listFiles();
        byte [] hasilByteArray;
        
        String extension = "";
        
        for (int i = 0; i < listOfFiles.length; i++) {
            if (id==1 && i%2==0){
                ByteArrayOutputStream bos = new ByteArrayOutputStream();
                if (listOfFiles[i].isFile()) {
                    System.out.println("File " + listOfFiles[i].getName());

                    int j = listOfFiles[i].getName().lastIndexOf('.');
                    if (j > 0) {
                        extension = listOfFiles[i].getName().substring(j+1);
                    }         

                    BufferedImage originalImage = ImageIO.read(new File(FOLDER_PATH_SOURCE+"/"+listOfFiles[i].getName()));
                    ImageIO.write(originalImage, extension, bos);
                    bos.flush();
                    byte[] imageInByte = bos.toByteArray();
                    hasilByteArray=rm.bufferByte(imageInByte);


                    InputStream in = new ByteArrayInputStream(hasilByteArray);
                    BufferedImage image = ImageIO.read(in); 
                    ImageIO.write(image, extension, new File("e:/hasil/"+listOfFiles[i].getName()));
                    extension = "";

                    bos.close();
                }
            }
            else if (id==2 && i%2==1){
                ByteArrayOutputStream bos = new ByteArrayOutputStream();
                if (listOfFiles[i].isFile()) {
                    System.out.println("File " + listOfFiles[i].getName());

                    int j = listOfFiles[i].getName().lastIndexOf('.');
                    if (j > 0) {
                        extension = listOfFiles[i].getName().substring(j+1);
                    }         

                    BufferedImage originalImage = ImageIO.read(new File(FOLDER_PATH_SOURCE+"/"+listOfFiles[i].getName()));
                    ImageIO.write(originalImage, extension, bos);
                    bos.flush();
                    byte[] imageInByte = bos.toByteArray();
                    hasilByteArray=rm.bufferByte(imageInByte);


                    InputStream in = new ByteArrayInputStream(hasilByteArray);
                    BufferedImage image = ImageIO.read(in); 
                    ImageIO.write(image, extension, new File("e:/hasil/"+listOfFiles[i].getName()));
                    extension = "";

                    bos.close();
                }
            }
        }
        
    
    /*mengirim byte array untuk di proses oleh server*/
        
        
        
    /*mengelola byte array menjadi image grayscale*/
        
    }   
}
