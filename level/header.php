<?php
/**
 * The header for our theme.
 *
 * This is the template that displays all of the <head> section and everything up until <div id="content">
 *
 * @link https://developer.wordpress.org/themes/basics/template-files/#template-partials
 *
 * @package Level
 */

?><!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo( 'charset' ); ?>">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="profile" href="http://gmpg.org/xfn/11">
<link rel="pingback" href="<?php bloginfo( 'pingback_url' ); ?>">
<?php wp_head(); ?>
</head>

<body <?php body_class(); ?>>
	

    
<div id="page" class="site">

	<a class="skip-link screen-reader-text" href="#content"><?php esc_html_e( 'Skip to content', 'level' ); ?></a>


	<?php get_template_part( 'template-parts/top'); ?>
	<br>
	<br>
	<div class="col-md-2 col-md-offset-2" rowspan="3">
			&nbsp; <a h href="http://www.igc.usp.br/" target="_blank"><img src="<?php echo get_template_directory_uri();  ?>/imagens/logoigc" class="logo"></a>
		
			&nbsp; <a href="https://www.ime.usp.br/" target="_blank"><img src="<?php echo get_template_directory_uri();  ?>/imagens/logo" class="logo"></a>
	
			&nbsp; <a href="http://www5.usp.br/" target="_blank"><img src="<?php echo get_template_directory_uri();  ?>/imagens/usp-logo-png" class="logo"  width="185"  height="100" alt="" border="5" style="position:relative; left: 3px; top: 3px;"></a>
	</div>
	<div><a class="navbar-brand"><h3>&nbsp;SISTEMA DE CATALOGAÇÃO DE SEDIMENTOS</h3></a></div>


	<?php if ( has_header_image() ) { ?>

<div class="header-area"><img src="<?php header_image(); ?>" height="<?php echo get_custom_header()->height; ?>" width="<?php echo get_custom_header()->width; ?>" alt="" />
</div>
<?php } ?>
<div id="content" class="site-content">
	<div class="row">
	<?php if ( is_active_sidebar( 'below-navi' ) ) { ?>
	 <div class="medium-12 columns">
<div id="secondary" class="widget-area" role="complementary">
	<?php dynamic_sidebar( 'below-navi' ); ?>
</div><!-- #secondary -->
</div>
<?php } ?></div>