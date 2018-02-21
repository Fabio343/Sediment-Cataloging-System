<?php
/**
 * The main template file.
 *
 * This is the most generic template file in a WordPress theme
 * and one of the two required files for a theme (the other being style.css).
 * It is used to display a page when nothing more specific matches a query.
 * E.g., it puts together the home page when no home.php file exists.
 *
 * @link https://codex.wordpress.org/Template_Hierarchy
 *
 * @package Level
 */

get_header(); ?>

<div id="primary" class="content-area">
<main id="main" class="site-main" role="main">
	 <div class="col-sm-10 col-md-6">
            <div class="panel panel-default">
                <div class="panel-body">
                    <h4>Em Que Consiste o Sistema?</h4>
                    <p> É um acervo de exemplares de amostras de sedimentos de diversas regiões do mundo que podem ser usados para estudos,
                        de forma geral sendo principalmente focado em atividades didáticas da área de Geociências. </p>
                    <h4>Quem Pode Acessar?</h4>
                    <p>O acesso é livre a todos, sendo que as funções de alterações de qualquer informação são exclusivas aos administradores do sistema.</p>
                    <h4>Como Realizar Pesquisas?</h4>
                    <ul>
                        <li>Pode realizar a pesquisa por código da amostra, país, cidade, estado, ambiente, clima, entre outros.</li>
                    </ul>
                    <h4> Quais são as informações apresentadas na lista geral de Exemplares?</h4>
                    <p>Para cada amostra, é fornecida uma descrição geral com informações  como origem, tipo e granulometria</p>
                </div>
            </div>
        </div>	
       
        <a href="./wp-content/themes/level/downloads/arq.pdf" download="Arquivo de apoio">Baixe arquivos de apoio</a>
        <br>
        <div class="col-sm-10 col-md-8">
        <div class="panel panel-default">
        <a href="#janela70" class="Click Para Ter Acesso a Listagem Dos Países Listados Para Possíveis Dúvidas Durante As Pesquisas" rel="modal">Click Para Ter Acesso a Listagem Dos Países Listados Para Possíveis Dúvidas Durante As Pesquisas</a>
        </div>
        </div>
      
	      <div class="window" id="janela70">
		     <a href="#" class="fechar">X Fechar</a>
        <div align="left" id="test6" style="width:400px;height:400px;overflow-x:hidden;overflow-y:scroll;">
          <h4>Sigla Dos Países Listados Para Possíveis Dúvidas Durante As Pesquisas </h4>
          <h4>Sigla   / País    </h4>
          <h8>BR  /  Brasil</h8>
           <br>
          <h8>MV	/  Maldivas</h8>
           <br>
          <h8>GR  /  Grécia</h8>
           <br>
          <h8>CA	/  Canada</h8>
           <br>
          <h8>MX	/  México</h8>
           <br>
          <h8>FR  /  França</h8>
           <br>
          <h8>CL	/  Chile</h8>
           <br>
          <h8>NO	/  Noruega</h8>
           <br>
          <h8>CH	/  Suiça</h8>
           <br>
          <h8>CO	/  Colombia</h8>
           <br>
          <h8>NZ	/  Nova Zelândia</h8>
           <br>
          <h8>ES	/  Espanha</h8>
           <br>
          <h8>CR	/  Costa Rica</h8>
           <br>
          <h8>OM	/  Omã</h8>
           <br>
          <h8>RE	/  Reunião</h8>
           <br>
          <h8>EG	/  Egito</h8>
           <br>
          <h8>PE	/  Peru</h8>
           <br>
          <h8>US    /  Estados Unidos</h8>
           <br>
          <h8>DM	/  Dominica</h8>
           <br>
          <h8>PF	/  Polinesia Francesa</h8>
           <br>
          <h8>GB	/  Reino Unido</h8>
           <br>
          <h8>DK	/  Dinamarca</h8>
           <br>
          <h8>PY	/  Paraguai</h8>
           <br>
          <h8>PT	/  Portugal</h8>  
           <br>
          <h8>AE	/  Emiratos Arabes Unidos </h8>
           <br>
          <h8>AQ    /  Antartica</h8>
           <br>
          <h8> GF	/  Guiana Francesa</h8>
           <br>
         <h8> TW	/  Taiwan</h8>
           <br>
         <h8>AR    /  Argentina</h8>
           <br>
         <h8>GY	   /  Guiana</h8>
           <br>
         <h8> TR  /  Turquia</h8>
           <br>
         <h8>AW   /  Aruba</h8>
           <br>
         <h8> ID  /  Indonesia</h8>
           <br>
         <h8> UY  /  Uruguai</h8>
           <br>
         <h8>BS	 /  Bahamas</h8>
          <br>
         <h8>IL	 /  Israel</h8>
          <br>
         <h8>TH  /  Tailândia</h8>
          <br>
         <h8>AU	/  Australia</h8>
          <br>
         <h8>IS	/  Islândia</h8>
          <br>
         <h8>VE	/  Venezuela</h8>
          <br>
         <h8>BB	/  Barbados</h8>
          <br>
         <h8>IT	/  Italia</h8>
          <br>
         <h8>PR	/  Porto Rico</h8>
          <br>
         <h8>BO  /  Bolivia</h8>
          <br>
         <h8>JP	/  Japão</h8>
          <br>
         <h8>SE  /  Suecia</h8>
          <br>
         <h8>CV	/  Cabo Verde</h8>
          <br>
         <h8>MA	/  Marrocos</h8>
         <br>
         <h8>EQ	/  Equador</h8>
         <br>
        </div>
        </div>

        <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.1/jquery.min.js"></script>
		<script type="text/javascript">
			$(document).ready(function(){
				$("a[rel=modal]").click( function(ev){
					ev.preventDefault();
					var id = $(this).attr("href");
					var alturaTela = $(document).height(500);
					var larguraTela = $(window).width(500);
					//colocando o fundo preto
					$('#mascara').css({'width':larguraTela,'height':alturaTela});
					$('#mascara').fadeIn(1000);
					$('#mascara').fadeTo("slow",0.8);
					var left = ($(window).width(500) /2) - ( $(id).width(500) / 2 );
					var top = ($(window).height(500) / 2) - ( $(id).height(500) / 2 );
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

		<style>
		.window{
			display:none;
			width:900px;
			height:900px;
			position:absolute;
			left:0;
			top:0;
			background:#FFF;
			z-index:10000;
			padding:25px;
			border-radius:25px;
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

<br>
<h4>Exemplares recentes:</h4>
<br>
<div class="row small-up-1 medium-up-2 large-up-4 postbox">
   <?php while ( have_posts() ) : the_post(); ?>

        <?php

          /*
           * Include the Post-Format-specific template for the content.
           * If you want to override this in a child theme, then include a file
           * called content-___.php (where ___ is the Post Format name) and that will be used instead.
           */
          get_template_part( 'template-parts/content', get_post_format() );
        ?>

      <?php endwhile; ?>
      <?php /* Start the Loop */ ?>
      
      <?php if( class_exists( 'Jetpack' ) && Jetpack::is_module_active( 'infinite-scroll' ) ) {
        the_posts_navigation(); 
        } 
        else {
          level_paging_nav();
        }
        ?>
 </div>     
    
	<div class="row small-up-1 medium-up-2 large-up-4 postbox">
		<?php if ( have_posts() ) : ?>

			<?php if ( is_home() && ! is_front_page() ) : ?>
				<header>
					<h1 class="page-title screen-reader-text"><?php single_post_title(); ?></h1>
				</header>
			<?php endif; ?>

		

		<?php else : ?>

			<?php get_template_part( 'template-parts/content', 'none' ); ?>
		<?php endif; ?>
			</div><!-- #row -->
		</main><!-- #main -->
	</div><!-- #primary -->
<?php get_footer(); ?>
