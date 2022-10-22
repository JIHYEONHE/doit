package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.JOptionPane;
import javax.swing.SwingConstants;

public class MySwing09 extends JFrame {

	private JPanel contentPane;
	private JTextField tf; //번호가 출력될 곳
	String num = "";
	

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing09 frame = new MySwing09();
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
	public MySwing09() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 202, 263);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField();
		tf.setHorizontalAlignment(SwingConstants.RIGHT);
		tf.setBounds(12, 24, 133, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn1 = new JButton("1");
		btn1.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				click1();
			}
		});
		btn1.setBounds(12, 58,42, 23);
		contentPane.add(btn1);
		
		JButton btn2 = new JButton("2");
		btn2.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				click2();
			}
		});
		btn2.setBounds(63, 58,42, 23);
		contentPane.add(btn2);
		
		JButton btn3 = new JButton("3");
		btn3.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				click3();
			}
		});
		btn3.setBounds(106, 58,42, 23);
		contentPane.add(btn3);
		
		JButton btn4 = new JButton("4");
		btn4.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				click4();
			}
		});
		btn4.setBounds(12, 91,42, 23);
		contentPane.add(btn4);
		
		JButton btn5 = new JButton("5");
		btn5.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				click5();
			}
		});
		btn5.setBounds(63, 91,42, 23);
		contentPane.add(btn5);
		
		JButton btn6 = new JButton("6");
		btn6.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				click6();
			}
		});
		btn6.setBounds(106, 91,42, 23);
		contentPane.add(btn6);
		
		JButton btn7 = new JButton("7");
		btn7.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				click7();
			}
		});
		btn7.setBounds(12, 124,42, 23);
		contentPane.add(btn7);
		
		JButton btn8 = new JButton("8");
		btn8.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				click8();
			}
		});
		btn8.setBounds(63, 124,42, 23);
		contentPane.add(btn8);
		
		JButton btn9 = new JButton("9");
		btn9.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				click9();
			}
		});
		btn9.setBounds(106, 124,42, 23);
		contentPane.add(btn9);
		
		JButton btn0 = new JButton("0");
		btn0.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				click0();
			}
		});
		btn0.setBounds(12, 151,42, 23);
		contentPane.add(btn0);
		
		JButton btnCall = new JButton("CALL");
		btnCall.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				mycall();
			}
		});
		btnCall.setBounds(63, 151, 82, 23);
		contentPane.add(btnCall);
	}

	public void click1() {
		num += "1";
		tf.setText(num);
	}

	public void click2() {
		num += "2";
		tf.setText(num);
	}

	public void click3() {
		num += "3";
		tf.setText(num);
	}

	public void click4() {
		num += "4";
		tf.setText(num);
	}

	public void click5() {
		num += "5";
		tf.setText(num);
	}

	public void click6() {
		num += "6";
		tf.setText(num);
	}

	public void click7() {
		num += "7";
		tf.setText(num);
	}

	public void click8() {
		num += "8";
		tf.setText(num);
	}

	public void click9() {
		num += "9";
		tf.setText(num);
	}
	public void click0() {
		num += "0";
		tf.setText(num);
	}
	
	
	public void myclick(MouseEvent e) {
		JButton b = (JButton) e.getSource();
		String str_new = b.getText();
		String str_old = tf.getText();
		tf.setText(str_old+str_new);
	}
	public void mycall() {
		String str_tel = tf.getText();  //this는 나자신을 가리키는것 null도 가능
		JOptionPane.showMessageDialog(this, "calling" + str_tel);
	}

}
