<?php
/**
* @file
* Contains \Drupal\forcontu_hello\Controller\ForcontuPagesController.
*/
namespace Drupal\forcontu_pages\Controller;
use Drupal\Core\Controller\ControllerBase;
use Symfony\Component\HttpKernel\Exception\BadRequestHttpException;

/**
* Controller to return the content of the defined pages.
*/
class ForcontuPagesController extends ControllerBase {

  public function calculator($num1, $num2) {
    // a) we check that the values provided are numeric and
    // if they are not, we throw an exception
    if (!is_numeric($num1) || !is_numeric($num2)) {
      throw new BadRequestHttpException(t('No numeric arguments specified.'));
    }

    //b) The results will be displayed in HTML list format (ul).
    // Each element of the list is added to an array
    $list[] = $this->t("@num1 + @num2 = @sum",
                      ['@num1' => $num1,
                          '@num2' => $num2,
                        '@sum' => $num1 + $num2]);

    $list[] = $this->t("@num1 - @num2 = @difference",
                      ['@num1' => $num1,
                      '@num2' => $num2,
                      '@difference' => $num1 - $num2]);

    $list[] = $this->t("@num1 x @num2 = @product",
                      ['@num1' => $num1,
                      '@num2' => $num2,
                      '@product' => $num1 * $num2]);

    //c) Avoid division by zero error
    if ($num2 != 0){
      $list[] = $this->t("@num1 / @num2 = @division",
                        ['@num1' => $num1,
                        '@num2' => $num2,
                        '@division' => $num1 / $num2]);
    } else {
      $list[] = $this->t("@num1 / @num2 = undefined (division by zero)",
      array('@num1' => $num1, '@num2' => $num2));
    }
    
    //d) The $list array is transformed into an HTML list (ul).
    $output['forcontu_pages_calculator'] = [
    '#theme' => 'item_list',
    '#items' => $list,
    '#title' => $this->t('Operations:'),
    ];

    //e) The render array with the output is returned.
    return $output;
  }
} //class closure
