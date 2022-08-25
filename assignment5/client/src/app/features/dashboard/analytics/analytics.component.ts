import {
  ChangeDetectionStrategy,
  Component,
  OnDestroy,
  OnInit,
  ViewEncapsulation,
} from '@angular/core';
import { Router } from '@angular/router';
import { Subject, takeUntil } from 'rxjs';

import { DashboardService } from '../dashboard.service';

@Component({
  selector: 'analytics',
  templateUrl: './analytics.component.html',
  encapsulation: ViewEncapsulation.None,
})
export class AnalyticsComponent implements OnInit, OnDestroy {
  data: any;
  barChart1Data! :{x:string[],y:number[]}
  barChart2Data! :{x:string[],y:number[]}
  pieChart1Data! :{x:{'value':number,'name':string}[]};
  pieChart2Data! :{x:{'value':number,'name':string}[]};
  areaCharts = ['first', 'second', 'third', 'fourth'];
  private _unsubscribeAll: Subject<any> = new Subject<any>();

  /**
   * Constructor
   */
  constructor(
    private _dashboardService: DashboardService,
    private _router: Router
  ) {}

  // -----------------------------------------------------------------------------------------------------
  // @ Lifecycle hooks
  // -----------------------------------------------------------------------------------------------------

  /**
   * On init
   */
  async ngOnInit() {
    console.log('previous',this.barChart1Data)
    this._dashboardService.getBarChartOneDta().subscribe((res:any)=>{
      this.barChart1Data=res;
      console.log('barchart1datah',this.barChart1Data)
    })
    console.log('previous',this.barChart2Data)
    this._dashboardService.getBarChartTwoDta().subscribe((res:any)=>{
      this.barChart2Data=res;
      console.log('barchart2datah',this.barChart2Data)
    })
    console.log('previous',this.pieChart1Data)
    this._dashboardService.getPieChartOneDta().subscribe((res:any)=>{
      this.pieChart1Data=res;
      console.log('piechart1datah',this.pieChart1Data)
    })
    console.log('previous',this.pieChart2Data)
    this._dashboardService.getPieChartTwoDta().subscribe((res:any)=>{
      this.pieChart2Data=res;
      console.log('piechart2datah',this.pieChart2Data)
    })
  }


  /**
   * On destroy
   */
  ngOnDestroy(): void {
    // Unsubscribe from all subscriptions
    this._unsubscribeAll.next(null);
    this._unsubscribeAll.complete();
  }

  // -----------------------------------------------------------------------------------------------------
  // @ Public methods
  // -----------------------------------------------------------------------------------------------------

  /**
   * Track by function for ngFor loops
   *
   * @param index
   * @param item
   */
  trackByFn(index: number, item: any): any {
    return item.id || index;
  }

  // -----------------------------------------------------------------------------------------------------
  // @ Private methods
  // -----------------------------------------------------------------------------------------------------

  /**
   * Fix the SVG fill references. This fix must be applied to all ApexCharts
   * charts in order to fix 'black color on gradient fills on certain browsers'
   * issue caused by the '<base>' tag.
   *
   * Fix based on https://gist.github.com/Kamshak/c84cdc175209d1a30f711abd6a81d472
   *
   * @param element
   * @private
   */
}
