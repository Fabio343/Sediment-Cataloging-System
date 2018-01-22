<?php
/**
 * The template for displaying the footer.
 *
 * Contains the closing of the #content div and all content after.
 *
 * @link https://developer.wordpress.org/themes/basics/template-files/#template-partials
 *
 * @package Level
 */

?>

	</div><!-- #page --></div><!-- #content -->
<div id="footer-widget">
<div class="row">
<div class="large-3 columns">
	<?php dynamic_sidebar( 'footer-1' ); ?></div>
<div class="large-3 columns">
	<?php dynamic_sidebar( 'footer-2' ); ?></div>
<div class="large-3 columns">
	<?php dynamic_sidebar( 'footer-3' ); ?></div> 
<div class="large-3 columns">
	<?php dynamic_sidebar( 'footer-4' ); ?></div>
</div>
</div>

	<footer id="colophon" class="site-footer" role="contentinfo">
		
		<div class="row">
		<div class="small-12 medium-6 large-6 columns">
		<div class="site-info">
	
			<span class="sep"> </span>
			
			<a>
					<br>
                     © 2016 - 2018
                    <br>
                      Instituto De Geociências-USP
                     <br>
                    Universidade De São Paulo
                </a>
                <br>
                <a href="https://github.com/Fabio343/Sediment-Cataloging-System" target="_blank">GitHub</a>
				 <a href="#janela0"  rel="modal"><h5>Créditos</h5></a>
                      <div class="window"  id="janela0">
                      <a href="#" class="fechar">X Fechar</a>
                       <h8>Desenvolvimento:</h8>
                       <li>Fabio Carvalho de Souza; Aluno de Graduação, Matemática Aplicada e Computacional IME-USP</li>
                       <br>
                       <h8>Professor(a) Orientador(a)do Projeto:</h8>
                       <li>Christine Laure Marie Bourotte; Professora do Departamento de Geologia Sedimentar e Ambiental IGC-USP</li>
                       <br>
                       <h8>Professor(a) Orientador(a)do Projeto:</h8>
                       <li>Kelly Rosa Braghetto; Professora Doutora Do Departamento de Ciência Da Computação IME-USP</li>
                       <br>
                       <h8>Progama de Bolsas Unificadas USP: </h8>
                        <li>Projeto: Desenvolvimento De Um Banco De Dados Sistematizado Para A Coleção De Areias Utilizada Para Fins Didáticos E De Difusão Em Geociências.</li>
                      </div>
                      <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.1/jquery.min.js"></script>
		<script type="text/javascript">
			$(document).ready(function(){
				$("a[rel=modal]").click( function(ev){
					ev.preventDefault();
					var id = $(this).attr("href");
					var alturaTela = $(document).height();
					var larguraTela = $(window).width();
					//colocando o fundo preto
					$('#mascara').css({'width':larguraTela,'height':alturaTela});
					$('#mascara').fadeIn(1000);
					$('#mascara').fadeTo("slow",0.8);
					var left = ($(window).width() /2) - ( $(id).width() / 2 );
					var top = ($(window).height() / 2) - ( $(id).height() / 2 );
					$(id).css({'top':top,'left':left});
					$(id).show();
 				});
 				$("#mascara").click( function(){
 					$(this).hide();
 					$(".window").hide();
 				});
 				$('.fechar').click(function(ev){
 					ev.preventDefault();
 					$("#mascara").hide();
 					$(".window").hide();
 				});
			});
		</script>

		<style type="text/css">
		.window{
			display:none;
			width:700px;
			height:500px;
			position:absolute;
			left:0;
			top:0;
			background:#FFF;
			z-index:10000;
			padding:20px;
			border-radius:20px;
		}
		#mascara{
			position:absolute;
  			left:0;
  			top:0;
  			z-index:10000;
  			background-color:#000;
  			display:none;
		}
		.fechar{display:block; text-align:right;}
		</style>
		</div><!-- .site-info -->
		<?php if (has_nav_menu('footer')) {
		wp_nav_menu( array( 'theme_location' => 'footer','menu_id' => 'footerhorizontal', 'echo' => true,'depth' =>'1','fallback_cb' => false ) ); }?>	
		</div>
		<div class="small-12 medium-6 large-6 columns social">
		<?php
		/*
		** Template to Render Social Icons on Top Bar
		*/
			for ($i = 1; $i < 8; $i++) : 
			$social = get_theme_mod('level_social_'.$i);
			if ( ($social != 'none') && ($social != '') ) : ?>
			<a class="hvr-ripple-out" href="<?php echo esc_url( get_theme_mod('level_social_url'.$i) ); ?>"><i class="fa fa-<?php echo $social; ?>"></i></a>
			<?php endif;

		endfor; ?>

		</div>
		</div>
	</footer><!-- #colophon -->
<?php wp_footer(); ?>
</div></div>
</body>
</html>