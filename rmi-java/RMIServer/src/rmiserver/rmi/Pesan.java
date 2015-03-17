/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rmiserver.rmi;

import java.awt.Color;
import java.awt.color.ColorSpace;
import java.awt.image.BufferedImage;
import java.awt.image.BufferedImageOp;
import java.awt.image.ColorConvertOp;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.imageio.ImageIO;
import static jdk.nashorn.internal.objects.NativeRegExp.source;

/**
 *
 * @author Peni Sriwahyu
 */
public class Pesan extends UnicastRemoteObject implements rmiinterface.rmiInterface{
    public Pesan() throws RemoteException{
        
    }

    @Override
    public byte[] bufferByte(byte[] a) throws RemoteException , IOException{      
            InputStream in = new ByteArrayInputStream(a);
            BufferedImage image = ImageIO.read(in);
            byte [] imageByte;
                        
            ColorConvertOp colorConvert =new ColorConvertOp(ColorSpace.getInstance(ColorSpace.CS_GRAY), null);
            colorConvert.filter(image, image);
            
            ByteArrayOutputStream bos = new ByteArrayOutputStream();
            ImageIO.write(image, "JPG", bos);
            bos.flush();
            imageByte = bos.toByteArray();
            return imageByte;
            
    }

   
    @Override
    public String str(String name) throws RemoteException {
        String a = name + " 1111111111";
        return a;
    }

    @Override
    public ArrayList arlist(ArrayList<byte[]> byteFile, ArrayList<String> extFile) throws RemoteException, IOException {
        ArrayList<byte []> hasilArray = new ArrayList<>();
        for(int i=0; i<extFile.size(); i++){
                InputStream in = new ByteArrayInputStream(byteFile.get(i));
                BufferedImage image = ImageIO.read(in);
                byte [] imageByte;
                ColorConvertOp colorConvert =new ColorConvertOp(ColorSpace.getInstance(ColorSpace.CS_GRAY), null);
                colorConvert.filter(image, image);
                
                ByteArrayOutputStream bos = new ByteArrayOutputStream();
                ImageIO.write(image, extFile.get(i), bos);
                bos.flush();
                imageByte = bos.toByteArray();
                hasilArray.add(imageByte);
            }
        return hasilArray;
    }
  

}
