"use client"
import MyDay from '../../../../components/dashboard/calender/myday'
import MyTeamsDay from '../../../../components/dashboard/calender/myteamsday'
import Pageheader from '../../../../components/dashboard/common/pageheader'
import React from 'react';
import { useState } from 'react';

const title = 'Calender'

function Page() {
  const [activeTab, setActiveTab] = useState('MyDay');

  const myTabs = [
    { name: 'MyDay', href: '#', current: true },
    { name: 'MyMonth', href: '#', current: false },
    { name: 'MyYear', href: '#', current: false },
    { name: 'MyTeamsDay', href: '#', current: false },
  ];

  const actions = (
    <div className="page-header-actions">
      <button type="button" className="page-header-actions-button">
        Add Event
      </button>
    </div>
  );
  
  return (
    <div>
      <Pageheader 
        title={title} 
        tabs={myTabs} 
        actions={actions} 
        activeTab={activeTab} 
        setActiveTab={setActiveTab} 
      />
      {activeTab === 'MyDay' && <div>My Tasks <MyDay /></div>}
      {activeTab === 'MyMonth' && <div>Billing Content</div>}
      {activeTab === 'MyYear' && <div>Notifications Content</div>}
      {activeTab === 'MyTeamsDay' && <div>Notifications Content <MyTeamsDay /></div>}
    </div>
  );  
}
export default Page;