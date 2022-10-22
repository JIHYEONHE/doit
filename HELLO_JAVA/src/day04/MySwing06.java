package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing06 extends JFrame {

	private JPanel contentPane;
	private JTextField tfDan;
	JTextArea ta;
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing06 frame = new MySwing06();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 296, 298);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("출력단수 :");
		lbl.setBounds(42, 45, 57, 15);
		contentPane.add(lbl);
		
		tfDan = new JTextField();
		tfDan.setBounds(128, 42, 116, 21);
		contentPane.add(tfDan);
		tfDan.setColumns(10);
		
		JButton btn = new JButton("출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.setBounds(42, 73, 202, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(40, 106, 204, 145);
		contentPane.add(ta);
	}
	public void myclick () {
		String dan = tfDan.getText();  //입력 받는 단수 가져오기
		int idan = Integer.parseInt(dan); //입력 받은것 int숫자형으로 형변환
		
		String txt=""; //txt를 만들어서
		txt += idan+"*"+1+"="+(idan*1)+"\n";  //txt에 누적
		txt += idan+"*"+2+"="+(idan*2)+"\n"; 
		txt += idan+"*"+3+"="+(idan*3)+"\n"; 
		txt += idan+"*"+4+"="+(idan*4)+"\n"; 
		txt += idan+"*"+5+"="+(idan*5)+"\n"; 
		txt += idan+"*"+6+"="+(idan*6)+"\n"; 
		txt += idan+"*"+7+"="+(idan*7)+"\n"; 
		txt += idan+"*"+8+"="+(idan*8)+"\n"; 
		txt += idan+"*"+9+"="+(idan*9)+"\n"; 
		
		ta.setText(txt); //누적된 txt를 settext로 한번에 출력해준다.
		
//		int dan = Integer.parseInt(tfDan.getText());
//		String result = "";
//
//		for (int i = 2; i < 10; i++) {
//			result += dan + "*" + i + "=" + (dan * i) + "\n";
//		}
//		ta.setText(result);
		
	}
}
