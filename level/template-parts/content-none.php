<?php
/**
 * Template part for displaying a message that posts cannot be found.
 *
 * @link https://codex.wordpress.org/Template_Hierarchy
 *
 * @package Level
 */

?>

<section class="no-results not-found">
	<header class="page-header">
		<h3 class="page-title"><?php esc_html_e( 'Nenhum Resultado', 'level' ); ?></h3>
	</header><!-- .page-header -->

	<div class="page-content">
		<?php if ( is_home() && current_user_can( 'publish_posts' ) ) : ?>

			<p><?php printf( wp_kses( __( 'pronto para publicar seu primeiro post? <a href="%1$s">Comece aqui</a>.', 'level' ), array( 'a' => array( 'href' => array() ) ) ), esc_url( admin_url( 'post-new.php' ) ) ); ?></p>

		<?php elseif ( is_search() ) : ?>

			<p><?php esc_html_e( 'Desculpe, mas sua pesquisa não gerou resultados, tente com uma nova palavra chave.', 'level' ); ?></p>
			<?php get_search_form(); ?>

		<?php else : ?>

			<p><?php esc_html_e( 'Parece que não podemos encontrar o que você está procurando. Talvez a pesquisa possa ajudar.', 'level' ); ?></p>
			<?php get_search_form(); ?>

		<?php endif; ?>
	</div><!-- .page-content -->
</section><!-- .no-results -->
