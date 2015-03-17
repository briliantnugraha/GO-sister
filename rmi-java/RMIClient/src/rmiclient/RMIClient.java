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
import java.io.FileInputStream;
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
import rmiinterface.rmiInterface;

/**
 *
 * @author Peni Sriwahyu
 */
public class RMIClient {

    public final static String FILE_TO_SEND = "e:/gambar/1.PNG"; 
    public final static String FOLDER_PATH_SOURCE = "e:/gambar";
    public final static String FOLDER_PATH_DESTIN = "e:/hasil";
    
    public ArrayList<String> namaFile = new ArrayList<String>();
    public ArrayList<byte []> byteFile = new ArrayList<byte []>();
    public ArrayList<String> extFile = new ArrayList<String>();
    
    private void bacaFile() throws FileNotFoundException, IOException, RemoteException, NotBoundException{
    /*untuk menyambungkan client dengan server - getRegistry*/
        Registry reg = LocateRegistry.getRegistry("127.0.0.1", 5050);
        rmiInterface rm = (rmiInterface) reg.lookup("Echo");
       
    /*mengambil list file dan extensi*/
        File folder = new File(FOLDER_PATH_SOURCE);
        File[] listOfFiles = folder.listFiles();
        String extension = "";
        ByteArrayOutputStream bos = new ByteArrayOutputStream();
        for (int i = 0; i < listOfFiles.length; i++) {
            if (listOfFiles[i].isFile()) {
                System.out.println("File " + listOfFiles[i].getName());
                namaFile.add(listOfFiles[i].getName());
                
                int j = listOfFiles[i].getName().lastIndexOf('.');
                if (j > 0) {
                    extension = listOfFiles[i].getName().substring(j+1);
                }
                extFile.add(extension);
            }
            extension = "";
            
            BufferedImage originalImage = ImageIO.read(new File(FOLDER_PATH_SOURCE+"/"+listOfFiles[i].getName()));
            ImageIO.write(originalImage, extFile.get(i), bos);
            bos.flush();
            byte[] imageInByte = bos.toByteArray();
            byteFile.add(imageInByte);
        }
        bos.close();
        
    /*untuk membuat file image menjadi byte array
        ByteArrayOutputStream bos = new ByteArrayOutputStream();
        BufferedImage originalImage = ImageIO.read(new File(FILE_TO_SEND));
        ImageIO.write(originalImage, "PNG", bos);
        bos.flush();
        byte[] imageInByte = bos.toByteArray();
        bos.close();*/
        
        ArrayList<byte []> hasilByte = new ArrayList<>();
    /*mengirim byte array untuk di proses oleh server
        byte[] hasilImage = rm.bufferByte(imageInByte);*/
        hasilByte=rm.arlist(byteFile, extFile);
        
        
    /*mengelola byte array menjadi image grayscale
        InputStream in = new ByteArrayInputStream(hasilImage);
        BufferedImage image = ImageIO.read(in);
        ImageIO.write(image, "PNG", new File("d:/a.PNG"));*/
        for(int k=0; k<namaFile.size(); k++){
            InputStream in = new ByteArrayInputStream(hasilByte.get(k));
            BufferedImage image = ImageIO.read(in); 
            ImageIO.write(image, extFile.get(k), new File("e:/hasil/"+namaFile.get(k)));
        }
    }   
    
    
        
    public static void main(String[] args) throws IOException, FileNotFoundException, RemoteException, NotBoundException {
        RMIClient rmc = new RMIClient();
        rmc.bacaFile();
    }
    
}
